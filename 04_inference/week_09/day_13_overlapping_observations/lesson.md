# Day 13 — Overlapping Observations

## 1. Warm-up retrieval (no notes)

1. Why does shuffling a time series break the statistics computed
   from it?
2. A statistic's SE assumes iid observations. If observations are
   *positively* autocorrelated, is the naive SE too big or too small?
3. What is n_eff, and how do you estimate it from an ACF?

## 2. Why a quant needs this

Strategy returns are almost never observed at the frequency they are
*held*. A 5-day-holding strategy earns an H = 5 day return, but papers
sample that return **every day**: r_t, r_{t+1}, …, where r_t covers
days t…t+4 and r_{t+1} covers days t+1…t+5. Consecutive observations
share 4 of 5 days. They are not independent — and the naive SE says
they are. This is the most common quiet inflation of t-stats in the
factor literature, and it is fully predictable from H.

## 3. Intuition — the overlap is the autocorrelation

Two H-day overlapping returns, k days apart, share H − k of their
H days (for k < H). If daily returns are iid, the correlation is
exactly the shared fraction:

```
ρ_k = (H − k) / H        for k = 1, …, H−1;    ρ_k = 0 for k ≥ H
```

H = 5:  ρ = (0.8, 0.6, 0.4, 0.2) — a slow triangle of dependence.
H = 252 (monthly, overlapping 12 months of weekly data, as in JT93):
ρ decays almost linearly for a year. The naive t-stat sees N
"observations" where there are really N/H *independent* information
units.

## 4. The mathematics

**The SE correction (Bartlett / first-order Newey–West).** For a
stationary mean with ACF ρ₁…ρ_K:

```
Var(x̄) ≈ (σ²/n) · (1 + 2 Σ_{k=1}^{K} ρ_k)
t_corrected = t_naive / sqrt(1 + 2 Σ ρ_k)     (bigger SE, smaller t)
```

For the overlapping triangle, Σ_{k<H} (H−k)/H = (H−1)/2, so

```
1 + 2Σρ_k = 1 + (H−1) = H      ->      SE grows by sqrt(H)
```

**The full-sample identity: overlapping H-day sampling costs you a
factor of √H in precision.** A "t = 3.2" from 5-day overlapping data
is a t ≈ 3.2/√5 ≈ 1.4 — noise. (The Newey–West estimator in 06.8 is
the general version of this: kernel-weighted Σρ̂_k instead of the
exact triangle, with a chosen lag K ≈ √n.)

**When does it NOT bite?** Non-overlapping sampling (hold 5 days,
observe every 5 days): then the observations are independent (for iid
daily) and N shrinks but the SE per N is honest. The overlap is the
crime, not the low sample size.

## 5. Python implementation

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(3)
r = rng.normal(0, 0.01, 5000)                # iid daily, true mean 0
H = 5
R = pd.Series(r).rolling(H).sum()            # overlapping H-day returns
rho = [R.autocorr(k) for k in range(1, H)]
mult = np.sqrt(1 + 2*sum(rho))
t_naive = R.mean()/(R.std()/np.sqrt(len(R)))
t_corr = t_naive / mult
print(f"ACF(1..4) = {[f'{x:.2f}' for x in rho]}  (want 0.8, 0.6, 0.4, 0.2)")
print(f"t naive {t_naive:.2f} -> corrected {t_corr:.2f}  (factor {mult:.2f} ≈ √{H})")
```

The Monte-Carlo check that matters: repeat 1,000 times on pure null
data and count how often each version rejects at 5% — naive should
reject far more often than 5%; corrected ≈ 5%.

## 6. On real data

SPY: 5-day overlapping returns. The true (unknown) mean is what it
is — but the *procedure* is identical: ACF, Bartlett factor, corrected
t. Note the factor ≈ √5 even on real data: the overlap structure, not
the market, sets the correction.

```python
from qrc.data import get_prices
r = get_prices("SPY", start="2000-01-01").iloc[:, 0].pct_change().dropna()
R = r.rolling(5).sum()
mult = np.sqrt(1 + 2*sum(R.autocorr(k) for k in range(1, 5)))
t = R.mean()/(R.std()/np.sqrt(len(R)))
print(f"5-day overlap: naive t {t:.2f}, factor {mult:.2f}, corrected {t/mult:.2f}")
```

## 7. Research connection

- **Jegadeesh & Titman (1993):** weekly returns from 5-day-holding
  portfolios are *overlapping by construction* — their t-stats carry
  this structure; modern re-runs report Newey–West-adjusted values.
- **Newey & West (1987):** the HAC estimator generalizing the
  Bartlett factor to regression (06.8 implements it).
- **Kozłowski (2007), "The t-statistic of overlapping portfolios":**
  the formal small-sample correction (the simple √H rule is the large-n
  version; small N needs the refined one).

## 8. Common mistakes

1. **Naive t on overlapping returns.** The classic. Factor: √H for
   the triangle; a t = 2.9 at H = 5 is t ≈ 1.3. Direction always:
   *upward* inflation (positive ρ).
2. **"Monthly" ≠ independent.** Monthly returns sampled monthly from
   12-month overlapping portfolios are 11/12 correlated. Frequency
   labels do not tell you the design.
3. **Fixing it by thinning the sample.** Taking every 5th
   observation makes them independent *and* divides N by 5 — usually
   the right fix, but it discards information; Newey–West keeps all
   observations at the correct SE. Know both, say which you used.

## 9. Reflection

- The Bartlett factor uses *all* lags k < H with the exact triangle.
  Newey–West truncates at K ≈ √n with a kernel. If H > K (very long
  holding, short sample), NW under-corrects — what do you do then?
  (Increase K past H; or thin the sample; the two must be compared.)
- Overlap inflates the t of the *mean*. What does it do to the
  volatility estimate of the overlapping series? (It does not bias
  the level much, but its *SE* is wrong the same way — the |R| ACF
  argument from 04.1/04.9.)

## Self-check

1. H = 21 (weekly, 3-week holdings): the Bartlett factor; a paper's
   t = 3.5 on such data.
2. Your 5-day strategy has 1,500 overlapping daily observations.
   Equivalent independent sample size? One sentence on what that does
   to "N = 1,500" in your report.

---

**Answers:** (1) Factor = √H = 21 ≈ 4.58 → t ≈ 3.5/4.58 ≈ **0.76**
— noise. (Note: for H = 21 the exact triangle has 20 lags, sum =
10, factor = √21 exactly.) (2) 1,500/5 = **300** independent
information units. The honest sentence: "N = 1,500 overlapping
observations, equivalent to ≈ 300 independent; all SEs reported with
Newey–West (5 lags) — the naive t would be √5 ≈ 2.24× too large."
