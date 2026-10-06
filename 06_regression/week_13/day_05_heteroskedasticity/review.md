# Day 5 Review — Heteroskedasticity & White's Repair

## Retrieval (answers)

1. Heteroskedasticity: Var(ε_t) = σ_t² varies — by time regime (vol
   clustering), by |x|, or cross-sectionally (vol spreads). β̂ stays
   unbiased (A2 intact); classical SEs invalid.
2. Sandwich: (XᵀX)⁻¹ · meat · (XᵀX)⁻¹; White's meat = Σ e_t² x_tx_t′ —
   each observation's own squared residual as its variance witness.
3. HC1 = HC0 × n/(n−k) — the default df-flavored White (statsmodels:
   cov_type="HC1").
4. White fixes A4 only — NOT A5 (no off-diagonal lag terms) and NOT A2
   (no SE touches bias). Autocorrelation needs Newey–West (day 8).
5. Detection: fan plot (|e| vs x, time-bucketed var(e)); White test:
   auxiliary regression e² ~ x + x², n·R² ~ χ².

## Elaboration prompts

- Explain to a skeptic why estimating n variances from n residuals ("one
  parameter each!") is consistent anyway. (Consistency lives in the
  *average* meat, not the individual e_t².)
- Your White SE came out SMALLER than classical. Is that a problem? What
  data configuration produces it, and what do you check before quoting
  either?

## Interleaved problem

A cross-sectional study regresses 2,000 stocks' next-month returns on
log-size. Classical SE 0.004, White SE 0.011, t drops from 5.1 to 1.9.
The authors ship the regression with *classical* SEs "for comparability
with the literature." Compose the referee paragraph — and state what
E4's ratio-table result implies about "the literature" they cite.

<details><summary>Reference answer</summary>

"In this cross-section, variance demonstrably scales with the regressor
(vol and the size factor covary; the White−classical gap of 2.75× is the
signature). The classical t = 5.1 is computed under an assumption the data
reject; the White t = 1.9 is the honest statement of the precision. 'For
comparability' is precisely backwards: the cited literature's classical
t-stats were plausibly overstated by the same mechanism (the ratio error
is direction-random across settings but rarely zero), and comparability
with overstated statistics is not a virtue. Report both SEs, headline the
White one, and temper the claim to what t ≈ 1.9 supports." E4's lesson:
you cannot repair the literature by rule — only paper by paper, honest SE
by honest SE.
</details>

## Self-grade

- Sandwich written from memory, bread/meat named?
- White's reach (A4 yes; A5, A2 no) cold?
- The detection pair (fan plot, White test) ready to run?
