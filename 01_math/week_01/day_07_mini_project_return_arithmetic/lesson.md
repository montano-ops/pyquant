# Day 7 — Mini-Project: Return Arithmetic You Can Trust

## The brief

You will build a **personal research toolkit** — small, tested functions for
return arithmetic — and then use it to answer three questions where the
wrong arithmetic produces confidently wrong research. This toolkit follows
you through the entire course; everything later (Sharpe ratios, factor
returns, backtests) calls these primitives.

**Build (in the exercise notebook, top cell):**

```python
import numpy as np
import pandas as pd

def to_log(simple):     ...
def to_simple(logret):  ...
def cagr(simple, ppy=252): ...        # geometric mean, annualized
def ann_vol(simple, ppy=252): ...     # ddof=1, sqrt-scaling
def total_growth(simple): ...         # prod(1+r)
def drawdown(simple): ...             # the growth/cummax()-1 series
```

Every function gets **three tests**: (1) a hand-computable case,
(2) an identity case (e.g., `to_simple(to_log(x)) == x`), and (3) a
property case (e.g., CAGR of a constant 1% daily series = 10.95% annual —
compounding, not 252%).

**Then answer (with your toolkit, on SPY + one volatile asset — real or
synthetic):**

- **Q1 — The drag, measured.** Arithmetic-annualized return vs CAGR for each
  asset. Which asset pays more drag? Does the σ²/2 approximation match the
  measured gap (report both)?
- **Q2 — Frequency illusion.** Compute daily returns and monthly returns
  from the *same* prices. Compare monthly CAGR computed (a) by compounding
  monthly returns, (b) by annualizing the mean daily return. Same number?
  Which is honest growth, and which is a promise no investor received?
- **Q3 — Volatility scaling check.** Annualized vol computed from daily
  returns (×√252) vs from monthly returns (×√12). Close? Why are they *not*
  identical (hint: squared returns don't sum linearly when vol clusters —
  you'll formalize this in module 09)?

**Write the reflection:** which of the three wrong-arithmetic traps is most
tempting *to you*? Where did your toolkit's tests catch a mistake during
development?

## Rules

- Write tests *before* trusting outputs. A wrong primitive poisons
  everything above it — this is why real research code has tests at all.
- All functions must handle a pd.Series in, pd.Series/float out.
- Document each function with one line: what it assumes, what it returns.

Done means: toolkit + tests green + Q1–Q3 answered with numbers + reflection.
The solution notebook shows an exemplar implementation and a worked analysis.
