# Day 9 — Joint Distributions and Two-Asset Portfolios

## Warm-up retrieval (no notes)

1. Cov(X,Y) in words; the normalization to get ρ; its range.
2. SE of a 63-day sample correlation under independence?
3. Why does calm-period diversification fail in crashes?

## 1. Why a quant needs this

Variance of a sum needs the joint behavior of the parts. Today: the joint
distribution, the covariance term in full, and the two-asset portfolio as
the complete worked example — the formula you will use in some form every
week from now on.

## 2. Joint distributions: two variables, one cloud

A joint distribution is the full likelihood pattern of (X, Y) *together*.
Visualize a scatter cloud: its center (means), its per-axis spread
(variances), its tilt (covariance). Marginals = per-axis views (what you
see if you ignore the other variable); the *tilt* is invisible in
marginals — which is why two assets can look individually tame and combine
badly, or look wild and combine well.

```python
import numpy as np
rng = np.random.default_rng(7)
rho = 0.6
z1, z2 = rng.standard_normal(2000), rng.standard_normal(2000)
y1 = z1
y2 = rho * z1 + np.sqrt(1 - rho**2) * z2       # correlated pair by construction
```

## 3. Variance of a sum — the theorem with the covariance term

$$\text{Var}(aX + bY) = a^2\text{Var}(X) + b^2\text{Var}(Y) + 2ab\,\text{Cov}(X, Y)$$

The third term is where portfolios live. Derivation-flavored intuition:
when both are above their means together (positive cov), the sum's
extremes compound; when one is up while the other is down (negative cov),
extremes cancel. **Special cases to memorize:**

- Independence: Var(X+Y) = Var(X) + Var(Y) — variance *adds*, so SD adds as
  √(sum) — the √n law and the √252 annualization, both now *derived*.
- Perfect hedge (ρ = −1, equal σ): Var(X+Y) = 0 — the only truly
  riskless combination.

## 4. The two-asset portfolio (everything on one page)

$$\mu_p = w\mu_1 + (1-w)\mu_2$$
$$\sigma_p^2 = w^2\sigma_1^2 + (1-w)^2\sigma_2^2 + 2w(1-w)\rho\,\sigma_1\sigma_2$$

```python
import numpy as np
mu1, mu2, s1, s2, rho = 0.0006, 0.0003, 0.012, 0.010, 0.2
w = np.linspace(0, 1, 101)
var = w**2*s1**2 + (1-w)**2*s2**2 + 2*w*(1-w)*rho*s1*s2
print(f"min-vol weight on asset 1: {w[np.argmin(var)]:.2f}")
```

Explore (in the exercise): the frontier's shape for ρ ∈ {−1, 0, 0.3, 1} —
including the fact that for ρ < 1, min-variance weights are NOT 100% in the
lower-vol asset. Correlation changes not just risk but *optimal
construction* — the mathematical seed of all portfolio theory.

## 5. On real data: hedging, measured

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT"], start="2010-01-01")
r = px.pct_change().dropna()
cov, var_m = r["SPY"].cov(r["TLT"]), r["SPY"].var()
beta_hedge = -cov / var_m                    # the weight on TLT that minimizes hedged variance
hedged = r["SPY"] + beta_hedge * r["TLT"]
print(f"unhedged vol {r['SPY'].std():.4%} -> hedged {hedged.std():.4%}")
```

(The minimizing weight is $-\text{Cov}/\text{Var}$ — take it on faith today
as calculus; it's day 11-module-01's regression slope with a sign flip.
Module 06 formalizes; you've now used it twice.)

## 6. Research connection

- The entire factor-model research program: decompose joint variation into
  common factors + idiosyncratic noise — a structured model of the joint
  distribution (module 07).
- Minimum-variance and risk-parity construction (module 11) is this page
  scaled to N assets.
- Momentum's long-short spread *is* a two-asset portfolio (winners minus
  losers) whose variance contains the W–L covariance — when losers and
  winners crash together (2009), the spread's variance explodes: momentum
  crashes are a covariance event (Daniel & Moskowitz, module 07.18).

## 7. Common mistakes

- Dropping the covariance term "to simplify" — the error behind naive risk
  aggregation (and behind 2008's "our CDO tranches are diversified"
  arithmetic).
- Confusing the minimum-*variance* weight with the maximum-Sharpe weight —
  today's formula only knows risk; μ enters tomorrow's questions.
- Assuming the estimated (μ, σ, ρ) triple *is* the truth — layer 2 vs
  layer 1 (day 5); ρ̂ alone has SE ≈ 1/√T.

## 8. Reflection

1. Why does ρ < 1 make the min-variance portfolio hold *some* of the
   higher-vol asset? Say it with the covariance term.
2. Design a false conclusion from ignoring the W–L covariance in a
   long-short backtest (hint: 2009).

**Self-check:** write Var(aX+bY) and the two-asset portfolio formulas from
memory; derive the √n law from the independence case.
