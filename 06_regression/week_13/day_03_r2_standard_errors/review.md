# Day 3 Review — R², Standard Errors, t-Stats

## Retrieval (answers)

1. R² = 1 − SSE/SST — variance share explained; with one regressor +
   intercept, R² = corr². In-sample fit only.
2. Var̂(β̂) = σ̂²(XᵀX)⁻¹, σ̂² = SSE/(n−k); one regressor: SE(β̂) =
   σ̂_e/(σ̂_x√n) — noise up, √n down, x-spread down.
3. t = β̂/SE, df = n−k; CI = β̂ ± t₀.₉₇₅·SE; "95%" is a property of the
   *procedure across parallel worlds*, not the one interval you got.
4. Calibration: indices-on-indices R² ~0.9; stock-on-market ~0.2–0.4;
   honest predictive regressions ~0.0x — and can still matter economically.
5. Simulation meaning of SE: the SD of β̂ across re-drawn histories; the
   formula is the shortcut that avoids re-drawing.

## Elaboration prompts

- Without formulas: why does more spread in x shrink SE(β̂)? (A wider
  lever arm: the same residual wobble tips the fitted line less.) Now name
  the market phenomenon that gives you spread for free.
- Explain to a junior why "the CI says where beta *was measured to be*
  in this window, not where beta *will be*" — and which day of this course
  charges for confusing the two.

## Interleaved problem

A fund shows: "beta of our hedge = 0.90, t = 45, R² = 0.62" on 6 months of
daily data (n = 126). (a) Recover SE(β̂) from the t. (b) Using the closed
form with σ_e/σ_x ≈ 0.79√((1−R²)/R²)... simpler: from SE and n, estimate
SE at 3 years. (c) The CIO asks: "the hedge is 0.90 — I'll short 0.90
units." Write the two-sentence risk note.

<details><summary>Reference answer</summary>

(a) SE = 0.90/45 = 0.020. (b) SE scales as 1/√n: SE_3y = 0.020·√(126/756)
≈ 0.008 — *if* the world stayed the same, the 3-year estimate would be
tighter; but (c) is the real answer. (c) "The 0.90 is measured to ±0.04
(95%) *within these six months*, which were [choose: calm/crisis] — a
regime, not a constant; hedge leakage out-of-window is the norm (day 17),
so size the short with the CI, not the point estimate, and re-fit on a
schedule. A hedge sized off t = 45's *point* estimate owns the estimation
distribution's tails on the day it matters."
</details>

## Self-grade

- SE closed form + the matrix formula, both, cold?
- Coverage definition of the CI stated correctly (procedure vs one-world)?
- The three R² calibration bands memorized with their reasons?
