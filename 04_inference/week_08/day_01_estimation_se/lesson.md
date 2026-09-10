# Day 1 — Estimation & Standard Error

## 1. From description to inference

Module 03 described; module 04 *argues*. An estimator x̂ is a rule
applied to a sample; its realized value is a draw from a sampling
distribution (03.2); **inference is reasoning from the draw to the
parameter.** Three properties that make an estimator worth arguing
from:

- **Consistency**: x̂ → θ as n → ∞ (more data, less error — eventually).
- **Unbiasedness**: E[x̂] = θ at any n (no systematic tilt).
- **Efficiency**: smallest sampling variance among candidates.

The sample mean is all three for μ (under iid); the sample max is
consistent for the max but says nothing honest about the tail beyond it;
a winsorized mean is biased-but-efficient (03.2's trade — the MSE
identity bias² + variance is the ledger).

## 2. The SE, one more time — now as the engine of inference

Every test, CI, and p-value this module is a rearrangement of one
object: the **standard error** — the sampling SD of the estimator.

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
n = len(r)
print(f"x̄ = {r.mean():.5%}, s = {r.std():.4%}, n = {n}")
print(f"SE(x̄) = s/√n = {r.std()/np.sqrt(n):.5%}")
print(f"signal/noise: |x̄|/SE = {abs(r.mean())/(r.std()/np.sqrt(n)):.2f}")
```

That last line is a t-statistic — previewed in module 02.5's E4, built
formally on day 4. Everything this week is: **estimate ± k·SE**.

## 3. SEs for the statistics finance actually uses

| Estimator | SE (large n) | Finance use |
|---|---|---|
| Mean x̄ | s/√n | mean return, alpha |
| Difference of means | √(s₁²/n₁ + s₂²/n₂) | strategy vs benchmark |
| Variance s² | s²·√(2/n) | vol estimates |
| Skew, kurtosis | √(6/n), √(24/n) | shape (03.4) |
| Correlation ρ̂ (ρ=0) | 1/√T | factor relationships (02.8) |

The **difference of means** row is new and central: comparing a
strategy to its benchmark is the *paired* case (same dates) when the
returns align — then SE(diff) = SD(strategy − benchmark)/√n, usually
far SMALLER than the independent formula (the market cancels). Day 8
(week 9) builds the formal paired test; today, know why pairing is a
variance-reduction gift: **shared noise cancels, private noise
remains.**

```python
# paired vs independent SE, felt
from qrc.data import get_prices as gp
px2 = gp(["SPY", "TLT"], start="2010-01-01")
d = px2.pct_change().dropna()
diff = d["SPY"] - d["TLT"]
se_paired = diff.std()/np.sqrt(len(diff))
se_indep = np.sqrt(d["SPY"].var()/len(d) + d["TLT"].var()/len(d))
print(f"SE(diff): paired {se_paired:.5f} vs independent {se_indep:.5f}")
```

## 4. Where finance's SEs go wrong (the standing caveats)

The formulas above assume iid. Returns give you three violations, each
with a known direction:

1. **Fat tails** (03.4): small-sample SEs of mean-based statistics are
   understated — t-stats computed at n=60 run hot (day 4 quantifies).
2. **Volatility clustering** (03.10): n_eff < n for anything volatility-
   sensitive; the honest SE multiplies by √(n/n_eff) — often 1.2–1.8×.
3. **Regimes/non-stationarity** (03.9): the "parameter" you estimate is
   itself a moving target; no SE fixes a misspecified question.

**The professional habit:** compute the textbook SE, then state which
of the three caveats applies and in which direction it pushes. The
naive SE is the *floor* of your uncertainty.

## 5. The one identity to carry

t ≈ estimate/SE — "how many standard errors from zero." Once you see
every result in finance as (estimate, SE), papers transform: stars on
coefficients are t-statistics; "significant" means |t| > 2; "the effect
is 4.2 SEs from zero" is a sentence you can interrogate (how was the SE
computed? under which assumptions?).

## Self-check

1. Why is a paired difference's SE usually smaller than the independent
   formula's?
2. Your strategy's mean return has textbook SE 0.010%. Give two
   reasons the honest SE is larger, with directions.
3. Estimator A: unbiased, variance 4. Estimator B: bias 1, variance 1.
   MSE of each? When is B preferable?

---

**Answers:** (1) Common market movement cancels in the subtraction —
only the idiosyncratic difference carries variance. (2) Fat tails:
small-sample t inflated, SE understated; clustering: n_eff < n → SE ×
√(n/n_eff). Both push the same way: the truth is *less* significant
than the textbook number. (3) MSE_A = 4, MSE_B = 1 + 1 = 2 — B wins
whenever the bias is small relative to the variance it kills (the
shrinkage logic; module 09's covariance shrinkage is this at scale).
