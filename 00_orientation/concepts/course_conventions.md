# Course Conventions (reference)

These conventions are used in every notebook. Internalize them once; they never change.

## Data shapes

- **Prices/returns are wide DataFrames**: rows = dates (a `DatetimeIndex` of trading days), columns = tickers.
- **Signals and positions are wide too** — same shape as returns, so they multiply elementwise.
- One asset? Still a one-column DataFrame or a named Series, not bare arrays.

## The two return definitions

| | simple return | log return |
|---|---|---|
| formula | r_t = P_t/P_{t-1} − 1 | r_t = ln(P_t/P_{t-1}) = ln(1 + r_t) |
| combines over time | multiply: (1+r1)(1+r2)… | add: r1 + r2 + … |
| combines across assets | weighted sum of simple returns ✓ | NOT a weighted sum (log of a sum ≠ sum of logs) |
| floor | −100% | unbounded below (but price stays > 0) |
| course default for **time aggregation** | ✓ (CAGR, compounding) | ✓ (nice for statistics) |
| course default for **portfolios & backtests** | ✓ | ✗ |

Rule of thumb (refined in 01.3): log ≈ simple when |r| is small; they diverge in crashes.

## Time discipline (the most important convention in the course)

A position you decide using information from day *t* earns the return of day
*t+1*. In pandas that means **`positions = signal.shift(1)`** before
multiplying by returns. Every backtest bug that produces "too good to be true"
is some version of forgetting this. You will meet it formally in module 08,
build the invariant into your engine in module 12, and hunt it in module 13.

## Data access

```python
from qrc.data import get_prices          # downloads once, caches to data/cache/*.parquet
from qrc.synth import synthetic_prices   # offline, seeded, realistic fat tails + vol clustering
```

Every notebook starts with `DATA_SOURCE = "real"` or `"synthetic"`.

## Code style for research

- Small named steps, not clever one-liners — you will read this code in six months.
- Fixed seeds for every random process; the seed is part of the result.
- Plot early, plot often; label axes (future-you reads plots, not memories).
- When a number matters, print it with a label, don't leave it as the last expression of a cell.

## The reflection questions (asked every single day)

1. What did I learn?
2. What assumption does this method make?
3. How could this analysis mislead me?
4. What would I test next?
