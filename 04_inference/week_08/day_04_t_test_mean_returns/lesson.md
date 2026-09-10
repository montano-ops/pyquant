# Day 4 — The t-Test for Mean Returns

## 1. The workhorse, assembled

You already own every part: t = x̄/(s/√n) = (estimate)/(SE), compared
to the t-distribution (fatter-tailed than normal at small n — exactly
fat enough to correct for estimating σ). Under H₀: μ=0 with iid
normal-ish returns, t ~ t(n−1).

```python
from qrc.data import get_prices
import numpy as np
from scipy import stats
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
n = len(r)
t_stat = r.mean()/(r.std(ddof=1)/np.sqrt(n))
print(f"t = {t_stat:.2f}, p = {2*(1-stats.t.cdf(abs(t_stat), n-1)):.4f}")
print(f"scipy check: {stats.ttest_1samp(r, 0)}")
```

Real SPY since 1993: t ≈ 3–4 on daily returns — the drift is real but
it took ~7,500 days to say so with confidence. **The same arithmetic at
one-year scale (n=252, mean/σ ≈ 0.04) gives t ≈ 0.6: one year of daily
data cannot distinguish buy-and-hold from a coin.**

## 2. The identity that runs the literature: t = SR·√(years)

For a return series: t = √n · (x̄/s) = SR_daily·√(252·Y) = **SR_annual·
√Y** where Y = years of data. Rearranged:

> **Years to reach t = 2: Y = (2/SR)².**

| True Sharpe | Years to t=2 | Years to 80% power (one-sided 5%) |
|---|---|---|
| 1.0 | 4 | 6 |
| 0.7 | 8 | 13 |
| 0.5 | 16 | 25 |
| 0.3 | 44 | 69 |

*(Verify the power column in day 7's lab; it's 80% power ≈ t_needed =
1.645 + 0.84 = 2.49 SEs.)*

**This table is why most published strategies are unverifiable within a
career at honest Sharpe levels — and why module 13's "deflated Sharpe"
exists.** When a paper reports a Sharpe of 0.6 on 5 years (t = 1.34,
not significant), or 0.4 on 3 years (t = 0.69), the honest reading is
"unmeasured," not "working."

## 3. Reading JT (1993) Table 1 through this lens

Jegadeesh & Titman's momentum spreads: monthly WML ≈ 0.95%/mo with
t-statistics ≈ 3–4 over 1965–1989 (25 years → t = SR·√25 = 5·SR → the
implied Sharpe of the monthly spread ≈ 0.6–0.8). The paper's stars are
this table's rows. **Every t-stat in every factor paper is SR·√Y in
disguise** — and the question to ask of each is whether the Sharpe it
implies is one you'd trade, and whether the Y it used is one that
wasn't mined (week 9's day 04.11; Harvey–Liu–Zhu's whole thesis).

## 4. Where the t-test breaks on returns

The test assumes iid, normal-ish sampling of the mean. Returns deliver:

1. **Fat tails** (κ ≈ 10, module 03.4): the t-statistic's own tail is
   fatter than t(n−1) at small n → **nominal 5% tests reject at 6–9%**
   under the null. At n ≥ 500, CLT repairs it (02.15); at n = 60
   (monthly strategy), it does not.
2. **Vol clustering** (03.10): SE understated by √(n/n_eff) — t runs
   hot by the same factor. A t of 2.3 under clustering is a t of ~1.6–
   1.9 in truth.
3. **Serial correlation in the strategy's returns** (smoothed
   positions, overlapping portfolios — JT's ARE overlapping!): positive
   autocorrelation inflates t dramatically (week 9's day 04.13, HAC
   preview).

```python
# fat-tail size distortion, measured
rng = np.random.default_rng(4)
rej = 0
for _ in range(5000):
    x = rng.standard_t(5, 60)/np.sqrt(5/3)*0.01   # t(5), sigma=1%, n=60
    t = x.mean()/(x.std(ddof=1)/np.sqrt(60))
    rej += abs(t) > 2.0
print(f"nominal 5% test, t(5) parent, n=60: rejects {rej/50:.1f}%")
```

**Runs ≈ 6–8%.** Your "significant" monthly strategy at n=60 with fat
tails is significant at a true level of ~7% — multiply its p-value by
1.5 mentally and see if you still like it.

## 5. The professional's t-test checklist

Before trusting any t-stat: n and frequency (→ CLT coverage); parent's
kurtosis (→ small-n distortion); autocorrelation of the series (→ SE
inflation; HAC needed if overlapping); multiplicity context (how many
siblings?); and the implied Sharpe (t/√Y) — is it even *plausible*?
**A t-stat is a claim about an SE; the SE is a claim about the data's
dependence. Interrogate the SE, not the star.**

## Self-check

1. A paper: "alpha t = 2.1, 36 months, overlapping positions." List the
   three corrections in order of likely severity.
2. Your strategy: Sharpe 0.45, live for 2 years. What does t = 0.45·√2
   ≈ 0.64 NOT tell you? What would?
3. Why does the t-distribution (not normal) apply, and why does that
   correction become irrelevant at n=1000 while the fat-tail problem
   doesn't?

---

**Answers:** (1) Overlapping positions → serial correlation → SE
understated (biggest; HAC/04.13); n=36 monthly with fat tails → small-
sample distortion (+1.5–2× on p); multiplicity (how many strategies
were tried?). (2) Not: that the strategy has no edge (t=0.64 is
consistent with SR 0.45 AND with 0); would: a power statement — "if SR
were 0.5, 2 years rejects ~15% of the time" — and the monitoring plan
(day 7's lab builds exactly this). (3) The t-distribution corrects for
estimating σ from the same sample — that correction vanishes as n
grows (t → normal). The fat-tail problem is about the PARENT's tails,
not the estimator's — the CLT eventually fixes the mean's sampling
distribution, but "eventually" is n ≈ 500+ at daily fat-tail levels.
