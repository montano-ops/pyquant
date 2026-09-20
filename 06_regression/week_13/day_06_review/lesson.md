# Day 6 — Review: Days 1–5

Cold retrieval, then problems. Commit to answers before checking. NO NOTES —
if you can't produce it cold, it's not yours yet, and the honest move is to
log it and re-derive it.

## Cold retrieval

1. The OLS minimization problem, and the two-variable closed form for β̂
   and α̂. What does "scaled covariance" mean?
2. `np.linalg.solve` over `inv`: why, in one line each of speed and
   numerical stability.
3. The three residual identities (with intercept) and which ones fail
   without one.
4. R² = 1 − SSE/SST; its corr² identity; the three calibration bands for
   returns regressions.
5. Var̂(β̂) = σ̂²(XᵀX)⁻¹ and the one-regressor closed form
   SE(β̂) = σ̂_e/(σ̂_x√n). Name each term's direction of influence.
6. A1–A6 from memory, each with what it buys and where returns data breaks
   it.
7. The failure hierarchy: which assumption breaks unbiasedness, which break
   only inference, which is nearly cosmetic at research n.
8. White's sandwich: bread and meat, what the meat replaces, and which
   assumptions White does NOT repair.
9. The OVB formula and its two corollaries.
10. Coverage: what "95% CI" is a claim *about* (procedure vs one world).

## Interleaved problems

**P1.** n = 1000, σ_e = 0.012, σ_x = 0.008. Compute SE(β̂) and the ±95%
half-width on β. Your PM wants the half-width below 0.01 — what does n
have to be?

**P2.** Regression of QQQ on SPY, daily, one year: β̂ = 1.18, SE = 0.05.
A friend says "QQQ is about 18% more volatile than the market." Identify
the confusion and compute the vol ratio implied if corr = 0.95.

**P3.** Your residual ACF at lags 1–5 reads [0.42, 0.35, 0.31, 0.24, 0.22]
from a regression of *21-day overlapping* returns. Which assumption,
which repair, which lag choice?

**P4.** In E2(b)-style data (variance rising with |x|), someone reports
classical SE 0.030 and t = 4.0 for β̂ = 0.12. Roughly what t do you expect
under White, and what does the corrected t do to the claim?

**P5.** "We winsorized the residuals at 1%/99% to fix heteroskedasticity."
Two objections, one of which previews day 11.

## Build (20 min)

From a blank notebook: `ols_fit(x, y)` returning coefficients, both SE
flavors (classical + White HC1), t's, R², residuals — verify against
statsmodels on a planted world (β known), then fit one real (or synthetic)
market-model regression and print the audit line: var(e) by time quintile,
ACF(e) lags 1–5, excess kurtosis. This is the drill every later module
assumes you can run cold.

## Error log

One line, this week: which assumption did you personally under-weight
before day 4's tournament, and what number changed your mind? (The
rejection-rate column is the persuasive one — 21% and 37% are not typos,
they are what naive t-stats *do* in finance data.)
