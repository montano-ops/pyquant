# Day 1 — Prices: Raw vs Adjusted

## 1. Three price series, three different claims

| Series | What it is | What returns from it measure |
|---|---|---|
| `raw_close` | the as-traded price | the *price* return — ignores dividends, breaks at splits |
| `adj_close` (provider) | raw × cumulative adjustment factor | the *total* return of a holder who reinvests |
| `close` (auto-adjusted) | raw × split-only factor | price return, split-repaired |

**Research uses total-return series.** A backtest on raw prices of a
dividend-paying stock understates the holder's return by the dividend
yield (~1.5–2%/yr for the S&P historically, 3–5% in high-yield eras)
and reads every ex-dividend day as a crash: a $1 dividend on a $40
stock is a −2.5% "loss" that never happened to the holder.

## 2. The compounding gap, felt

```python
from qrc.data import get_prices
import numpy as np
adj = get_prices("SPY", start="1993-02-01", field="adj_close")["SPY"]
raw = get_prices("SPY", start="1993-02-01", field="raw_close")["SPY"]
print(f"total-return growth: {adj.iloc[-1]/adj.iloc[0]:.1f}x")
print(f"price-only growth:   {raw.iloc[-1]/raw.iloc[0]:.1f}x")
```

**The same ticker, the same decades: total return compounds to
several times the price-only multiple.** SPY since 1993: roughly 13–14×
from price alone vs 18–20× with dividends reinvested (exact values
move with the window — the gap, ~0.5×/decade of yield compounding, is
the point). Any long-horizon study that used raw closes silently
deleted a third of the equity premium.

## 3. The anatomy of an adjustment

Adjusted price at time t:

> adj_t = raw_t × F_t,  where F_t = Π (adjustment events after t)

A $2 dividend on a $100 stock tomorrow makes today's raw close
overstate yesterday-equivalent value by ~2% — so the provider divides
all PAST prices by (1 + div/price) at each ex-date. Splits multiply
instead: a 2:1 split halves all past prices. **Adjusted series change
retrospectively**: yesterday's stored adj_close for 2010 is not
necessarily today's — a new dividend rewrites history. (Cache
implication: re-pull or recompute adjustments; never mix adjusted
series pulled at different times.)

## 4. Total-return reconstruction from raw + actions

The holder's return on day t:

> r_t = (P_t + D_t) / P_{t−1} − 1

where D_t is the dividend that went ex on day t (splits neutralized
first). This is the CRSP convention, and it is *exactly* what you
rebuild by hand tomorrow. The provider's adj_close gives the same
returns (up to reinvestment timing):

> r_t = adj_t / adj_{t−1} − 1

## 5. Where each series is the RIGHT one

- **Backtests, factor sorts, anything return-based** → adjusted
  (total return). No exceptions.
- **Execution realism** (what price could you actually trade?) → raw
  close/open of the day, with the adjusted series used only for
  signal computation. Mixing these up = trading a price that never
  existed.
- **Position sizing / share counts** → raw price × shares; the
  adjusted price is a synthetic construct.
- **Charts for humans** → raw (people remember actual price levels);
  **charts for research** → adjusted (levels are meaningless across
  actions anyway).

**The classic bug:** signal on adjusted, execute at raw, size at
adjusted — three different price universes in one backtest. One price
series per purpose, stated in the methodology.

## 6. Synthetic check (works offline)

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(0)
n = 500
raw = 100 * np.exp(np.cumsum(rng.normal(0.0003, 0.01, n)))     # a "stock"
div_dates = pd.date_range("2020-01-01", periods=n, freq="B")[::63]
divs = pd.Series(1.0, index=div_dates)                          # $1 quarterly
# holder's total return with cash dividends (no reinvestment):
r_price = pd.Series(raw).pct_change()
holder = r_price + divs.reindex(r_price.index).fillna(0) / pd.Series(raw).shift(1)
print(f"price return total: {np.prod(1 + r_price.fillna(0)) - 1:+.1%}")
print(f"holder total return: {np.prod(1 + holder.fillna(0)) - 1:+.1%}")
```

The holder beats the price by roughly (yield × years) compounded —
on synthetic numbers, a few dozen bp; on real dividend payers, the
percentage-point-scale gap of §2.

## Self-check

1. A 2:1 split occurs today. What happens to adj_close history
   overnight? What happens to raw_close history?
2. Why does a raw-close backtest make dividend stocks look WORSE, not
   just equal? (Ex-div days read as losses → long-only signals
   penalized; and the terminal wealth misses the yield.)
3. Your signal fires on adjusted closes; your backtest fills at raw
   closes. Name the specific trade where this creates a phantom edge.

---

**Answers:** (1) adj history: all past prices halve (the cumulative
factor absorbs the split); raw history: unchanged — splits only
rewrite the adjusted construct. (2) Both mechanisms: ~2%/yr missing
yield AND ex-div days manufacturing −1 to −3% "returns" that trigger
stop-losses, vol estimates, and mean-reversion signals. (3) Any
ex-dividend day: the signal sees adjusted (smooth), the backtest
fills at raw (down 2%) — a "buy the dip" that isn't there, or a stop
that shouldn't have fired. The arbitrage between the two price series
is pure fiction.
