# Day 8 — Covariance and Correlation

## Warm-up retrieval (no notes)

1. Write E[aX + bY] and the two conditions under which Var(X+Y) = Var(X)+Var(Y).
2. The three-layer stack: which layer do biases live on?
3. Expectancy of 55%/±1% daily for 252 days — roughly what's the SD of the
   year's total P&L (in return units)? (√n scaling.)

## 1. Why a quant needs this

Module 01 computed $\mathbf{w}^\top\Sigma\mathbf{w}$ mechanically. Today the
*objects inside* Σ — covariance and correlation — become probabilistic
quantities you can reason about, and you meet the two errors that ruin
portfolios: trusting correlation where it doesn't apply (crises), and
reading it as causation.

## 2. The definitions (population form)

$$\text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)], \qquad
\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

Covariance: the *expected product of deviations* — when X is above its
mean, is Y usually above (positive) or below (negative) hers? Units:
(return)² — awkward, which is why we normalize. Correlation: covariance on
a [−1, 1] scale — *the cosine of the angle* between centered variables
(day 8 of module 01, now official).

## 3. What ρ does and does not say

ρ measures *linear co-movement*:

- ρ = 0: no *linear* relationship (nonlinear dependence can hide here!)
- |ρ| = 1: perfect linear relationship
- sign: co-movement direction

It says **nothing about**: causation, timing, tails, or stability. Three
killer facts, each worth a career:

1. **Correlation ≠ causation**: ice-cream sales correlate with drownings
   (summer). In markets, nearly everything correlates with the market —
   most "discovered relationships" are shared exposure to a common factor
   (module 07 exists because of this).
2. **Correlations are conditional on regimes**: SPY–TLT was *positive*
   in the 1990s inflation era, negative for 2000–2021, and both near-zero
   and violently unstable across crises. A single full-sample ρ is an
   average over conditions that may never co-occur again.
3. **Tails break averages**: correlations estimated in calm periods rise
   toward 1 in crashes ("the only thing that goes up in a crash is
   correlation"). Diversification sized on calm-ρ fails at maximum
   drawdown — orientation day 7 Q5, now with the tool that explains it.

## 4. Estimation noise: ρ itself is a random variable

From T observations, the sample correlation has sampling noise ~
$1/\sqrt{T}$ (for true ρ=0: SE ≈ 1/√T). With T = 63 days, SE(ρ) ≈ 0.13: a
measured ρ = 0.25 sits at ~2 SE — borderline territory. Two independent
assets will show |ρ̂| > 0.25 about 5% of the time over a quarter, but
|ρ̂| > 0.13 (a single SE) about a third of the time. Quarter-length
correlations are soft clay: anything inside ±0.25 is compatible with
zero.

```python
import numpy as np
rng = np.random.default_rng(42)
rhos = []
for _ in range(2000):
    x, y = rng.standard_normal(63), rng.standard_normal(63)   # truly independent
    rhos.append(np.corrcoef(x, y)[0, 1])
rhos = np.array(rhos)
print(f"true rho = 0. sample: mean {rhos.mean():.3f}, sd {rhos.std():.3f}")
print(f"share |rho_hat| > 0.25: {(np.abs(rhos) > 0.25).mean():.1%}")
```

Run it. Internalize it: **short-window correlations are mostly noise.**
This one simulation kills a family of trading ideas (and explains why
module 09.16 shrinks covariance matrices).

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT", "GLD"], start="2006-01-01")
r = px.pct_change().dropna()
print(r.corr().round(3))
print(r["SPY"].rolling(252).corr(r["TLT"]).plot(title="1-year rolling SPY-TLT correlation"))
```

The rolling correlation wanders across regimes — the number your risk model
uses is a *draw*, not a constant.

## 6. Research connection

- The market model's β is Cov(r, r_m)/Var(r_m) — correlation's
  regression-scaled cousin (module 06.7 estimates it with uncertainty).
- Pairs trading (module 09) is a bet on a *stable* correlation/cointegration
  — and the strategy's blowups are exactly the historical moments where it
  broke.
- "Statistical significance of a correlation" is a t-stat of
  $\hat\rho\sqrt{T}/\sqrt{1-\hat\rho^2}$ — module 04 will let you test the
  claims you simulate today.

## 7. Common mistakes

- Reporting full-sample ρ as a property rather than an average over
  regimes.
- ρ = 0 read as "independent" (only uncorrelated *linearly*).
- Estimating ρ over short windows and trading on it (SE ≈ 1/√T — compute
  the SE before the trade).

## 8. Reflection

1. Your 63-day ρ̂ = 0.4 between two stocks. What range of true ρ is
   consistent with it (rough 2SE)? What should the trade sizing assume?
2. Give a false-trading-conclusion example: a correlation-based hedge that
   fails precisely when needed, with the mechanism named.

**Self-check:** write Cov and ρ; state three things ρ does not imply; give
the SE of ρ̂ under independence and its T-dependence.
