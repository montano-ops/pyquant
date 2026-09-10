"""qrc.data — market data access with a local parquet cache.

Design decisions you should notice (they are lessons, not accidents):

1. Caching is per (ticker, field): one download serves every future lesson.
2. `adj_close` and `raw_close` are DIFFERENT things on purpose — module 05
   makes you construct the adjustment yourself from raw prices + corporate
   actions, then compare with the provider's adjusted series.
3. Failures are loud. A missing ticker should stop your analysis, not
   silently shrink your universe (that is survivorship bias by try/except).
"""

from __future__ import annotations

import io
import urllib.request
import zipfile
from pathlib import Path
from typing import Iterable

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "data" / "cache"

# field -> (yahoo column, auto_adjust flag)
_FIELDS = {
    "adj_close": ("Adj Close", False),   # provider's dividend+split adjusted close
    "raw_close": ("Close", False),       # as-traded close (unadjusted)
    "close": ("Close", True),            # split+dividend adjusted (auto_adjust=True)
    "open": ("Open", True),
    "high": ("High", True),
    "low": ("Low", True),
    "volume": ("Volume", True),
}

# Ken French Data Library datasets we allow (name -> zip filename stem)
_FF_DATASETS = [
    "F-F_Research_Data_Factors_daily",
    "F-F_Research_Data_Factors",
    "F-F_Research_Data_5_Factors_2x3_daily",
    "F-F_Research_Data_5_Factors_2x3",
    "Mom_Factor_daily",
    "Mom_Factor",
    "F-F_ST_Reversal_Factor_daily",
    "F-F_LT_Reversal_Factor_daily",
]

_FF_BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/{}.zip"


def _cache_path(subdir: str, name: str) -> Path:
    d = CACHE_DIR / subdir
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{name}.parquet"


def _clean_series(s: pd.Series, name: str) -> pd.Series:
    s = s.dropna()
    s = s[~s.index.duplicated(keep="last")]
    if s.index.tz is not None:  # yfinance may return tz-aware timestamps
        s.index = s.index.tz_localize(None)
    s.index.name = "date"
    s.name = name
    return s.sort_index()


def _download_ticker(ticker: str, field: str) -> pd.Series:
    import yfinance as yf  # imported lazily: qrc must import fine without internet

    column, auto_adjust = _FIELDS[field]
    df = yf.download(ticker, start="1990-01-01", auto_adjust=auto_adjust, progress=False)
    if df is None or len(df) == 0:
        raise RuntimeError(f"no data returned for {ticker!r}")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    if column not in df.columns:
        raise RuntimeError(f"column {column!r} missing for {ticker!r}; got {list(df.columns)}")
    return _clean_series(df[column].astype(float), ticker)


def get_prices(
    tickers: str | Iterable[str],
    start: str | None = None,
    end: str | None = None,
    field: str = "adj_close",
    refresh: bool = False,
) -> pd.DataFrame:
    """Wide DataFrame of prices (rows=dates, columns=tickers), cached per ticker.

    Parameters
    ----------
    tickers : ticker or list of tickers, e.g. "SPY" or ["SPY", "TLT"]
    start, end : date strings ("2010-01-01"); None = everything cached/downloaded
    field : 'adj_close' (default), 'raw_close', 'close', 'open', 'high', 'low', 'volume'
    refresh : force re-download (ignore cache)

    Raises
    ------
    RuntimeError if any ticker cannot be fetched — listing the failures — because
    silently dropping failed tickers is how survivorship bias sneaks in.
    (If you are offline, use qrc.synth.synthetic_prices instead.)
    """
    if field not in _FIELDS:
        raise ValueError(f"field must be one of {sorted(_FIELDS)}, got {field!r}")
    if isinstance(tickers, str):
        tickers = [tickers]
    tickers = list(tickers)

    out: dict[str, pd.Series] = {}
    failures: list[str] = []
    for t in tickers:
        cache = _cache_path("prices", f"{t.replace('/', '_')}_{field}")
        if refresh or not cache.exists():
            try:
                s = _download_ticker(t, field)
                s.to_frame().to_parquet(cache)
            except Exception as e:  # noqa: BLE001 — report and continue with others
                failures.append(f"{t}: {type(e).__name__}: {e}")
                continue
        out[t] = pd.read_parquet(cache)[t]
    if failures:
        raise RuntimeError(
            "Could not fetch: " + "; ".join(failures)
            + "\nIf you are offline, set DATA_SOURCE='synthetic' in the notebook "
              "(qrc.synth.synthetic_prices) or pass refresh=True once online."
        )
    df = pd.DataFrame(out)
    df.index = pd.to_datetime(df.index)
    if start is not None:
        df = df.loc[df.index >= pd.Timestamp(start)]
    if end is not None:
        df = df.loc[df.index <= pd.Timestamp(end)]
    return df


def get_actions(ticker: str, refresh: bool = False) -> pd.DataFrame:
    """Dividends and stock splits for one ticker: columns ['Dividends', 'Stock Splits'].

    This is the raw material for building adjusted prices BY HAND in module 05.
    """
    cache = _cache_path("actions", ticker.replace("/", "_"))
    if refresh or not cache.exists():
        import yfinance as yf

        tk = yf.Ticker(ticker)
        actions = pd.DataFrame({"Dividends": tk.dividends, "Stock Splits": tk.splits})
        actions = actions.dropna(how="all").fillna(0.0)
        actions.to_parquet(cache)
    df = pd.read_parquet(cache)
    df.index = pd.to_datetime(df.index)
    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)
    return df.sort_index()


def _parse_ff_text(text: str, name: str) -> pd.DataFrame:
    lines = [ln for ln in text.splitlines() if ln.strip() != ""]
    header_i = next(i for i, ln in enumerate(lines) if "Mkt-RF" in ln)
    cols = lines[header_i].split()
    # 'Mkt-RF' can arrive as 'Mkt-RF' or 'Mkt-RF '; normalise whitespace variants
    rows = []
    for ln in lines[header_i + 1:]:
        parts = ln.split()
        tok = parts[0]
        # data rows: date token (6 or 8 digits) + one value per column
        if not (tok.isdigit() and len(tok) in (6, 8)) or len(parts) != len(cols) + 1:
            break  # hit the annual footer / notes section
        rows.append(parts)
    raw = pd.DataFrame(rows)  # column 0 = date, then one column per factor
    freq_is_daily = len(raw.iloc[0, 0]) == 8
    idx = pd.to_datetime(raw.iloc[:, 0], format="%Y%m%d" if freq_is_daily else "%Y%m")
    df = raw.iloc[:, 1:].astype(float)
    df.columns = cols
    df.index = idx
    df.index.name = "date"
    df.columns = [c.strip() for c in df.columns]
    return df


def get_ff(name: str = "F-F_Research_Data_Factors_daily", refresh: bool = False) -> pd.DataFrame:
    """Download (and cache) a Ken French Data Library dataset.

    Examples: 'F-F_Research_Data_Factors_daily' (Mkt-RF, SMB, HML, RF — daily),
    'F-F_Research_Data_5_Factors_2x3_daily', 'Mom_Factor_daily'.
    Full list: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
    """
    if name not in _FF_DATASETS:
        raise ValueError(f"unknown dataset {name!r}; allowed: {_FF_DATASETS}")
    cache = _cache_path("ff", name)
    if refresh or not cache.exists():
        url = _FF_BASE.format(f"{name}_CSV")
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                blob = resp.read()
        except Exception as e:  # noqa: BLE001
            raise RuntimeError(
                f"could not download {url} ({type(e).__name__}: {e}). "
                "You need internet access the first time; the result is then cached."
            ) from e
        with zipfile.ZipFile(io.BytesIO(blob)) as zf:
            member = zf.namelist()[0]
            text = zf.read(member).decode("latin-1")
        _parse_ff_text(text, name).to_parquet(cache)
    df = pd.read_parquet(cache)
    df.index = pd.to_datetime(df.index)
    return df
