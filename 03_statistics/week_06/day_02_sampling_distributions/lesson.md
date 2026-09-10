# Day 2 — Sampling Distributions

## 1. A statistic is a random variable

Compute the mean of this decade → x̄₁. Recompute on a different window →
x̄₂. Different. The statistic itself has a distribution — the **sampling
distribution** — and knowing it is the difference between a number and an
estimate.

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()

# non-overlapping 2-year windows (504 days): the mean as a moving target
means = [r.iloc[i:i+504].mean() for i in range(0, len(r)-504, 504)]
print([f"{m:.4%}" for m in means])
```

**Expected sight:** 2-year means scattered from ≈ 0.02%/day to ≈ 0.08%/day,
some maybe negative. Same asset, same "strategy" (buy and hold) — the
*statistic* wanders. Any performance number you've ever seen is one draw
from a distribution like this.

## 2. The standard error, manufactured

The CLT (module 02.15) says the sampling distribution of x̄ is
approximately N(μ, σ²/n). So SE(x̄) = σ/√n — *measurable*:

```python
rng = np.random.default_rng(0)
n = 252
se_clt = r.std() / np.sqrt(n)
se_sim = np.std([ rng.choice(r.values, n).mean() for _ in range(3000) ])
print(f"SE of a 252-day mean: CLT {se_clt:.6f} | simulated {se_sim:.6f}")
```

They agree (this is the bootstrap at work, and — on real data — they
agree *less* than independence would predict; vol clustering, module
02.19, widens the true SE. Note the gap; day 9 returns to it.)

## 3. Every statistic has one

| Statistic | SE (large n, normal-ish) | At n=252, σ=1% |
|---|---|---|
| Mean x̄ | σ/√n | 0.063% — the mean is barely resolved |
| SD s | σ/√(2n) | 0.045% — vol is resolved in weeks |
| Skew ν̂ | √(6/n) | 0.15 |
| Excess kurtosis k̂ | √(24/n) | 0.31 |
| Quantile (central) | √(p(1−p)/n)/f(q) | modest for the median |
| Quantile (tails) | explodes — 1/f(q) huge | the 1% VaR is nearly unmeasurable |

```python
# watch the quantile estimator struggle in the tail
rng = np.random.default_rng(1)
for q in [0.5, 0.1, 0.05, 0.01]:
    est = [ np.quantile(rng.choice(r.values, 252), q) for _ in range(1000) ]
    print(f"q={q}: SE of estimate {np.std(est):.4%}")
```

**The pattern to internalize:** center statistics are cheap, tail
statistics are ruinous, and moment statistics of order k pay for their
sensitivity with SEs that grow like √k. This table is the price list of
empirical finance.

## 4. Bias and variance — the two axes

An estimator can be:

- **Unbiased, noisy**: x̄ wobbles around μ (good, but slow).
- **Biased, precise**: winsorized vol (day 5) — deliberately biased
  toward stability, dramatically less noisy. Sometimes a *choice*.
- **Biased, noisy**: the worst quadrant — e.g., max drawdown measured on
  an in-sample-optimized backtest. Most published Sharpe ratios live
  here (module 13 quantifies the bias).

**The trade:** mean-squared error = bias² + variance. Real practice
trades a little bias for a lot of variance reduction all the time
(shrinkage — module 09's covariance estimators are the flagship example).
What is *never* acceptable is bias you didn't know you had.

## 5. The reporting standard, effective today

From this day forward, in this course, a bare number in your notebooks is
a bug. The standard is:

> x̂ ± SE (n, window, data source)

`"The mean daily return is 0.041% ± 0.013% (n = 7,512, 1993–2023, CRSP
mirrors)"` — that sentence can be argued with, improved, replicated. The
bare `0.041%` can only be believed or ignored.

## Self-check

1. SE of the skew estimate at n = 1008 (4 years)? Can you distinguish
   skew −0.6 from 0 with one year of data?
2. Why is the 1% quantile's SE enormous *precisely because* returns are
   fat-tailed? (Two reasons: the density at the quantile is small; and
   fat tails make the sample sparse there.)
3. Your colleague reports median (not mean) returns "because it's more
   stable". What is the bias-variance trade they silently made?

---

**Answers:** (1) √(6/1008) ≈ 0.077; at n=252 SE ≈ 0.155 — one year cannot
separate −0.6 from 0 (it's under 2 SE); four years barely can. (2) SE of
a quantile ∝ 1/f(q): thin density at the quantile means few observations
near it, so the estimate jumps when the sample changes; fat tails thin
the density *and* add outliers that jerk the estimate. (3) The median is
robust (low variance) but estimates a *different quantity* than the mean
— for compounding wealth the log-mean is what matters; the median
silently ignores tail contributions to growth. They traded variance for
a change of question, not a better answer to the same question.
