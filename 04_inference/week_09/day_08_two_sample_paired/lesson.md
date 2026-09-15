# Day 8 — Two-Sample & Paired Tests

## 1. Warm-up retrieval (no notes)

1. Write the SE of the sample mean, and of the *difference* of two
   independent means.
2. What does the t-statistic equal, in words?
3. Your strategy's daily return has SD 1.2%. What is the SE of its mean
   over 252 days? Over 2,520?

(Answers: this week's earlier days + 03.2.)

## 2. Why a quant needs this

Every "strategy A beats strategy B" claim — including "my strategy beats
the benchmark" — is a two-sample problem. The subtlety is that in research
the two samples are almost never independent: **A and B earn returns on
the same dates**, share the same market shocks, and the market is usually
90%+ of both. Using the independent-sample formula on paired data is one
of the most common SE mistakes in performance-evaluation papers — and it
cuts both ways (usually it *overstates* the SE, but it can understate it
when the benchmark is the wrong one).

## 3. Intuition — the pairing dividend

Two strategies, 1,000 days each. Each return = market part + private part:
`A_t = m_t + a_t`, `B_t = m_t + b_t`. The difference:

```
A_t − B_t = (a_t − b_t)      ← the market part m_t CANCELS
```

The difference series has the variance of the *private* parts only. If
the market is 85% of the variance of each strategy, the difference is
roughly 15% of the individual variance — an SE **3× smaller** than the
independent formula claims. Pairing is not a technicality; it is the
difference between t = 0.8 (nothing) and t = 2.4 (a result).

**When is data "paired"?** Same time index *and* a shared driver that the
subtraction can cancel: same dates (always for daily strategy returns),
same portfolio of stocks before a factor tilt, two assets in the same
sector, before/after on the same asset. **When is it not?** Two strategies
on disjoint universes, or "this year vs that year" on the same index
(then the years are two samples of one process — closer to independent,
and regime differences contaminate the comparison).

## 4. The mathematics

**Independent (Welch) two-sample t.** Groups with n₁, n₂, means x̄₁, x̄₂,
variances s₁², s₂²:

```
t = (x̄₁ − x̄₂) / sqrt(s₁²/n₁ + s₂²/n₂),   df ≈ Welch–Satterthwaite
df = (s₁²/n₁ + s₂²/n₂)² / [ (s₁²/n₁)²/(n₁−1) + (s₂²/n₂)²/(n₂−1) ]
```

**Paired t.** Form the differences d_t = A_t − B_t on matched dates, then
it is a **one-sample t on the differences**:

```
t = mean(d) / (sd(d)/√n),   df = n − 1
```

Note what changed: the formula uses `sd(d)² = sA² + sB² − 2·ρ·sA·sB`. The
covariance term is the dividend. At ρ = 0 the two formulas agree; at
ρ = 0.9 with equal SDs, sd(d) = s·√(2−1.8) = 0.45·s vs s·√2 — the paired
SE is 2.2× smaller.

**Decision rule.** Matched time index → paired. Genuinely separate
samples → Welch. Same index but no shared driver (e.g. disjoint
universes) → Welch, and say so.

## 5. Python implementation

```python
import numpy as np, pandas as pd
from scipy import stats

rng = np.random.default_rng(7)
n = 1000
mkt = rng.normal(0, 0.01, n)                      # shared market
A = mkt + rng.normal(0, 0.003, n) + 0.00004       # strategy: edge 4bp/day
B = mkt + rng.normal(0, 0.003, n)                 # benchmark

t_ind, _ = stats.ttest_ind(A, B, equal_var=False) # Welch
d = A - B
t_paired = stats.ttest_1samp(d, 0.0).statistic    # paired
print(f"Welch t = {t_ind:.3f}   paired t = {t_paired:.3f}")
print(f"SE ratio: {t_paired/t_ind:.2f}x smaller when paired")
```

Verify Welch's df by hand on the same numbers, then build the *same* data
with the two strategies on **disjoint** universes (no shared `mkt`) and
confirm the two t-stats nearly agree.

## 6. On real data

Load two overlapping ETFs (e.g. SPY vs QQQ) and do both computations.
The paired t is the SE of the *active return* — the number an evaluation
actually needs.

```python
from qrc.data import get_prices
px = get_prices(["SPY", "QQQ"], start="2010-01-01")
r = px.pct_change().dropna()
d = r["QQQ"] - r["SPY"]
t = d.mean() / (d.std() / np.sqrt(len(d)))
print(f"QQQ−SPY: mean {d.mean():.5%}, paired t = {t:.2f}")
```

## 7. Research connection

Jegadeesh & Titman (1993) report t-stats on the **spread** portfolio
(W−L), not on each decile separately: that is a paired/one-sample design
on the difference — the shared market cancels, and the t-stats are much
tighter than comparing "decile 10 vs decile 1" as two independent
portfolios. Carhart (1997) factor regressions are the same move: the
intercept is tested on the *residual* series (market exposure removed
first) — pairing at the regression level.

## 8. Common mistakes

1. **Welch on paired data.** Overstates the SE (usually 2–5×) → real
   edges declared insignificant. The conservative error, but it kills
   research that was real.
2. **"Paired" by date coincidence.** Two strategies on unrelated
   universes share a calendar but no driver — subtracting still cancels
   the common market, which is *fine* for "does A have an edge vs B",
   but the difference is no longer the cleanest measure of the edge.
   Say which design you used and why.
3. **Overlapping observations treated as pairs of independent draws.**
   5-day-holding strategies resampled daily overlap 4/5 → the paired
   t itself is inflated. That is tomorrow's repair (day 04.13).

## 9. Reflection

- The paired design assumes the *pairing* is the source of shared
  variance. If the two series are cointegrated or share an unmodeled
  factor, the difference is non-stationary-ish or factor-driven — does
  that change the inference? (Module 09 revisits.)
- If a paper gives you means and SDs of two strategies but not the
  correlation of the difference, what can you bound the t-stat between?

## Self-check

1. Two strategies, same 500 days: SD each 1.0%, corr of the returns 0.9,
   mean difference 3bp. Paired t? Welch t? Which is the honest number
   and why?
2. When would the independent formula give a *smaller* SE than the
   paired one? (Think about the sign of the covariance.)

---

**Answers:** (1) sd(d) = 1.0%·√(2(1−0.9)) = 0.447%; SE = 0.447%/√500
= 2.0bp; paired t = 3/2.0 = **1.5**. Welch SE = √(1+1)/√500 = 2.83bp →
t = 1.06. Paired is honest: same dates, shared market. (2) When the
two series are *negatively* correlated — e.g. a long equity strategy vs
a short-equity benchmark, or equity vs a bond ETF: the covariance term
adds to the difference's variance, so pairing *increases* the SE. You
still use the paired formula (it's the correct design), but there is no
dividend — and a big negative correlation can make the comparison
statistically harder, not easier.
