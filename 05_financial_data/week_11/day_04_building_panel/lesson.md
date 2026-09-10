# Day 4 — Building a Panel

## 1. The panel is the research object

A single series is a column; research lives in the **panel**: dates ×
tickers, returns + signals + characteristics. Every factor study,
every backtest, every cross-sectional claim is a statement about a
panel — and the panel's CONSTRUCTION is where the biases live before
any statistic is computed.

## 2. The join, and its one crucial argument

```python
from qrc.data import get_prices
from qrc.universe import load_universe
tickers = load_universe("research50")[:8]
px = get_prices(tickers, start="2010-01-01", field="adj_close")
print(px.shape, "| NaNs per column:", px.isna().sum().tolist())
```

`pd.DataFrame(dict)` aligns on the UNION of dates (an outer join).
Alternatives change the sample:

- **outer** (default here): every date any ticker has → NaN where a
  ticker wasn't trading (pre-IPO, post-delist, holiday mismatches).
- **inner**: intersection — only days ALL tickers traded (drops each
  one's holidays; silently shrinks toward the most-restricted
  calendar; module 03.12's trap at panel scale).
- **ffill after outer**: fills pre-IPO gaps forward — WRONG: fills a
  stock's pre-existence with its first price backward in disguise
  (actually it leaves leading NaNs — pandas won't backfill by default
  — but ANY filling inside listing gaps fabricates flat returns).

**Rule: outer join, then keep NaN as NaN.** The NaN structure IS
information: it is the listing map.

## 3. Reading the NaN lattice

```python
import numpy as np
first_valid = px.apply(lambda s: s.first_valid_index())
last_valid = px.apply(lambda s: s.last_valid_index())
print(pd.DataFrame({"first": first_valid, "last": last_valid}))
```

Patterns and their meanings:
- **Leading NaNs**: IPO after the panel start (META: 2012) — the
  stock didn't exist; it is not "missing."
- **Trailing NaNs**: delisting/acquisition — the stock stopped; it
  did not "stop being interesting."
- **Interior NaNs**: halted trading, data vendor gaps, exchange
  holidays for foreign names — each needs a decision, logged.
- **All-NaN columns**: your ticker is wrong or the vendor failed —
  and `get_prices` raises loudly rather than dropping it (by design:
  silent drops are survivorship by try/except).

## 4. Returns from the panel (and the two classic bugs)

```python
r = px.pct_change()
```

Bug 1 — **the phantom return**: if a gap (halt) is followed by data,
pct_change computes a return across the gap — a "one-day" return that
is actually a week of news. Decide: NaN it (flag rows where the
previous price is >1 day old) or accept the approximation — stated.
Bug 2 — **adjusted-series staleness**: adj_close pulled in January
differs from adj_close pulled in March (new dividends rewrote
history); a panel built from mixed pulls has phantom returns on the
rewritten dates. Pull once, freeze, version.

## 5. Panel hygiene checklist (day 7's project makes it a habit)

1. One pull per field, one date, frozen; the pull is logged.
2. Outer join; NaNs preserved; listing map computed and reported.
3. Returns with the phantom-return check.
4. Per-ticker quality scan (module 03.5's outlier triage, at scale):
   |r|>25% verified, zero-runs, stale sequences.
5. A `panel_info` table: first/last dates, n, NaN %, action counts,
   min price, median dollar volume — the panel's ID card, printed at
   the top of every notebook that uses it.

## Self-check

1. Inner vs outer join on a US + Japan stock panel: what does each do
   to the sample, and which is right for a cross-sectional study?
2. Your panel has a stock with interior NaNs every third Tuesday.
   What are the three hypotheses, in order of probability?
3. Why is "drop all rows with any NaN" almost always the wrong
   cleaning for a panel?

---

**Answers:** (1) Inner: intersection calendar (drops each market's
holidays AND any halt — the sample becomes "days everything traded,"
over-weighting liquid calm days); outer: union with NaN gaps where
each market was closed — right for cross-sectional work because each
stock's returns are computed on its own trading days, and the NaN
structure is honest. (2) Vendor delivery schedule (weekly batch,
most likely), exchange half-days/holiday pattern (check the calendar),
genuine recurrent halts (least likely — and interesting if true).
(3) One dead stock deletes every other stock's rows on those dates —
the panel shrinks to the intersection of survivals: survivorship via
cleaning. Clean per-ticker or mask per-use, never dropna the panel.
