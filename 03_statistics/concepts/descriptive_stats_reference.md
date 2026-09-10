# Descriptive Statistics — Reference

## The two worlds

| | Population | Sample |
|---|---|---|
| Object | the full distribution (all possible days) | the days you actually observed |
| Notation | μ, σ, ν (skew), κ (kurtosis) | x̄, s, ĝ, k̂ |
| Nature | fixed, unknown | random — changes with the sample |
| The mistake | treating x̄ as μ | remembering x̄ is random |

One backtest = one sample. Two backtests of the same strategy on
neighboring windows = two draws. Day 1's whole point.

## Center

| Statistic | Breaks when | Use for returns because |
|---|---|---|
| Mean | one 1987 can move it | it's what compounds (log-mean ↔ growth) |
| Median | bimodal data hides | robust center for noisy samples |
| Trimmed mean (α) | asymmetric trimming distorts | a middle ground; winsorize = cap, trim = drop |

**The daily-returns reality:** mean ≈ 0.03–0.05%, SD ≈ 1% — the signal-to-
noise ratio is ~1:30. The mean is *barely* estimated by years of data
(module 02.12); the median of a positively-drifting series sits slightly
*below* the mean (right tail drags the mean up).

## Spread

| Statistic | Robust? | Notes |
|---|---|---|
| SD | no — one outlier rewrites it | the standard, because portfolio math uses variance |
| IQR | yes | middle 50%; survives crashes |
| MAD ×1.4826 | yes | scaled to match SD at normality |

## Shape

**Skewness** (moment version): ν = E[(z)³], z = (x−μ)/σ.
- ν < 0: long left tail — crashes. Equity indices: −0.3 to −1.
- ν > 0: long right tail. Single stocks mix; some strongly positive.
- SE(ν̂) ≈ √(6/n): at n=252, ±0.15 — a full year to tell −0.5 from 0.

**Excess kurtosis**: κ = E[(z)⁴] − 3.
- κ > 0: fat tails relative to normal. Equity indices: 2–20+ (daily).
- SE(k̂) ≈ √(24/n): at n=252, ±0.31.
- κ explodes with outliers: ONE 20σ day in 10 years of data contributes
  20⁴/2520 ≈ 32 to the estimate. Kurtosis is an outlier detector.

**Rank-based alternatives** (robust): skew via (mean − median)/σ or
Bowley; tail index via Hill estimator (module 09 territory). When the
moment estimators scream, check with these.

## Outliers & remedies

- **3σ rule fails twice**: fat tails mean real |z|>3 days (module 02.11);
  and σ̂ itself is contaminated by the outlier (masking).
- **Winsorize**: cap at the p/(100−p) percentiles. Keeps the day, shrinks
  its influence. Changes the mean less than the variance a lot.
- **Trim**: drop the extremes entirely. Report both trimmed and raw.
- **The golden rule**: never delete an outlier silently. It is the most
  informative point you own — 1987 is data, not dirt. Decide, document,
  and report both ways.

## The EDA liturgy (day 8 formalizes)

1. n, start/end, missingness — *before* anything else.
2. Headline stats: mean, SD, min, max, quartiles (the `.describe()` row).
3. Shape: histogram + KDE; skew & kurtosis **with SEs**.
4. Tails: QQ plot vs normal (the microscope — module 02.11).
5. Time structure: rolling mean & vol; ACF of r and |r|.
6. Verdict paragraph: what distribution is this *like*, and where does
   every candidate model break?

## Frequency choices (day 12)

| Frequency | n/year | Mean SE | Fat tails (κ) | Use |
|---|---|---|---|---|
| Daily | 252 | small | large (2–20) | default; vol clustering visible |
| Weekly | 52 | ×√5 wider | moderate | smoother, fewer crashes-in-isolation |
| Monthly | 12 | ×√21 wider | near-normal-ish | long-history comparisons; aggregational gaussianity |

Aggregational gaussianity (Cont fact #4): as you aggregate, tails thin —
the monthly-return distribution is much closer to normal than the daily.
CLT at work across time — but *slower* than independence implies
(dependence, module 02.19).
