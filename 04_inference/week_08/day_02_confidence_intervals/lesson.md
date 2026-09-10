# Day 2 — Confidence Intervals

## 1. What a CI actually is

x̄ ± 1.96·SE — the formula is trivial; the *reading* is where everyone
trips. The correct statement:

> **The procedure** "compute x̄ ± 1.96·SE from a random sample" covers
> the true μ in 95% of samples. THIS interval either contains μ or it
> doesn't — there is no probability left; the randomness was in the
> sample, not the parameter.

The two wrong readings: "there's a 95% probability μ is in this
interval" (μ isn't random in frequentist land) and "95% of future
returns fall in this range" (that's a prediction interval — vastly
wider; confusing the two is how "our expected return is 8% ± 2%" becomes
marketing).

## 2. See the coverage, don't believe it

```python
import numpy as np
rng = np.random.default_rng(0)
mu, sigma, n = 0.0004, 0.011, 252
cover = 0
for _ in range(1000):
    x = rng.normal(mu, sigma, n)
    lo, hi = x.mean() - 1.96*x.std(ddof=1)/np.sqrt(n), x.mean() + 1.96*x.std(ddof=1)/np.sqrt(n)
    cover += lo <= mu <= hi
print(f"empirical coverage: {cover/10:.1f}% (nominal 95%)")
```

≈95% of the 1,000 intervals catch μ. Rerun with n=30 and fat tails
(t(3) innovations): coverage sags toward 92–94% — **the 1.96 is
calibrated for normal-ish sampling; fat tails break small samples'
coverage** (the day-4 theme, arriving early).

## 3. CI for a mean return — the sobering arithmetic

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="2010-01-01")
r = px["SPY"].pct_change().dropna()
n = len(r); se = r.std()/np.sqrt(n)
print(f"mean {r.mean():.4%} ± {1.96*se:.4%} daily (n={n})")
print(f"annualized: [{(r.mean()-1.96*se)*252:+.1%}, {(r.mean()+1.96*se)*252:+.1%}]")
```

**The 15-year daily-mean CI annualizes to something like [1%, 14%].**
That is the honest uncertainty in "what does SPY earn per year" from 15
years of data. Any allocation memo that quotes a point estimate of
expected return without this band is fiction with footnotes.

## 4. The three things a wide CI tells you

1. **Not enough data**: n too small for the question. (Means are
   expensive — module 02.12's (2σ/μ)² law.)
2. **A noisy object**: the estimator's variance is intrinsic (high vol
   strategy → wide CI on its mean).
3. **Nothing about the point estimate's quality**: x̄ is still the best
   single guess; the CI is about *how loudly to hold opinions*.

**The practice:** every claim you write this week ends "…± 1.96·SE
(= CI)". A strategy with mean 0.06%/day ± 0.05%/day has a CI that
*straddles zero* — report that as the headline, not the 0.06%.

## 5. CI vs significance (the same coin)

| CI for μ | Two-sided test at 5% of H₀: μ=0 |
|---|---|
| excludes 0 | reject H₀ |
| includes 0 | fail to reject |

The duality: the 95% CI is the set of μ₀ values that a 5% two-sided
test would NOT reject. So "the CI includes zero" and "not significant
at 5%" are the same sentence — hold the equivalence; day 3 uses it.

## 6. CIs for Sharpe ratios (preview)

The SE of the Sharpe ratio itself: SE(SR̂) ≈ √((1 + SR²/2)/n) (per
period). At daily SR 0.03 (≈0.5 annual), n=252: SE ≈ 0.063 daily →
annualized SE ≈ 0.063·√252 ≈ 1.0 — **a one-year Sharpe estimate of 0.5
carries a 95% CI of roughly [−1.5, 2.5]**. The Sharpe you computed from
a one-year backtest is nearly uninformative about the true Sharpe.
(Module 12.15 gives the full treatment — MinTRL; day 7's lab measures
it by simulation.)

## Self-check

1. A 95% CI for a strategy's monthly mean is [−0.1%, +0.9%]. Translate
   into the significance statement and the business decision.
2. Why does quadrupling n only halve the CI width? What does that imply
   about "just get more data" for mean-return questions?
3. The prediction-interval confusion: construct a case where quoting
   the CI as "95% of returns" understates risk by 10×.

---

**Answers:** (1) Mean not distinguishable from 0 at 5% (duality); the
strategy is unproven — not necessarily bad; decision is whether the
CI's upper end justifies continued funding at your risk appetite.
(2) Width ∝ 1/√n: 4× data → 2× precision; for a mean-return edge
buried in 30× noise, 4× the years ≈ 8 years buys one halving — data is
bought in decades for means. (3) CI on the mean at daily scale is ~
±0.02%; the ±1.96σ band containing ~95% of *returns* is ±2%. Quoting
the CI as the return band shrinks perceived risk 100× — the classic
factsheet sin ("our expected daily return is 0.04% ± 0.02%" is not
"we lose at most 0.06% a day").
