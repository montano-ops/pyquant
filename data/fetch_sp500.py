#!/usr/bin/env python3
"""Snapshot the current S&P 500 constituent list from Wikipedia.

Writes data/cache/sp500_symbols_<YYYYMMDD>.csv so the snapshot date is recorded.

WARNING (this is the lesson, not a bug): this is TODAY's membership, not
point-in-time membership. Using it for historical backtests injects
survivorship + selection bias. Module 05 makes you measure the damage.
"""
from pathlib import Path

import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
CACHE = Path(__file__).resolve().parent / "cache"


def main() -> None:
    tables = pd.read_html(URL)
    df = tables[0]  # first table: Symbol, Security, GICS Sector, ...
    out = CACHE / f"sp500_symbols_{pd.Timestamp.today():%Y%m%d}.csv"
    CACHE.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"wrote {out} ({len(df)} constituents)")
    print("Remember: this list is dated TODAY, not point-in-time.")


if __name__ == "__main__":
    main()
