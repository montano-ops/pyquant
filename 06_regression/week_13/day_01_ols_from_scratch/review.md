# Day 1 Review — OLS from Scratch

## Retrieval (answers)

1. Min definition of OLS: min over (a, b) of Σ(y_t − a − b x_t)² — squared
   vertical deviations.
2. Normal equations: XᵀX β̂ = Xᵀy; one-regressor closed form: β̂ =
   cov̂(x,y)/vâr(x), α̂ = ȳ − β̂ x̄.
3. β = ρ·σ_y/σ_x — correlation scaled by relative volatility.
4. Why `solve` not `inv`: numerically stabler, faster, and fails less
   catastrophically under near-singularity.
5. No-intercept regression: forces the line through the origin — asserts
   α = 0; any mean level in y is pushed into β̂ (biased slope).

## Elaboration prompts

- Explain β without a formula, as if to a PM: "if the market does 1%, this
  position does about 1.2%, on average, over the estimation window" — then
  name the two weasel words ('about', 'window') and what each hides.
- Why do practitioners validate an estimator on a planted world before real
  data? What exactly does recovery of β = 1.20 prove, and what does it NOT
  prove?

## Interleaved problem

You regress a stock on the market, daily, 2000 obs: β̂ = 0.85, corr = 0.55,
σ_m = 0.9%, σ_s = 1.39%. (a) Verify β̂ from the closed form. (b) The same
regression on weekly returns (non-overlapping, ~417 obs) gives β̂ = 0.97.
Two candidate explanations: (i) the stock's market sensitivity genuinely
rises at the weekly horizon; (ii) estimation noise. Which SE must you
compute to tell them apart, and what is it approximately?

<details><summary>Reference answer</summary>

(a) β = 0.55 × 1.39/0.9 ≈ 0.849 — checks; β̂ is internally consistent with
the summary stats. (b) The horizon change is real structure ONLY if
|0.97 − 0.85| exceeds ~2 joint SEs. Daily SE(β̂) ≈ σ_e/(σ_m√n): σ_e ≈ σ_s·
√(1−ρ²) ≈ 1.16% → SE ≈ 0.0116/√2000 ≈ 0.026. Weekly σ_e ≈ 1.16%·√5 ≈ 2.6%,
σ_m ≈ 2.0%, SE ≈ 0.026/0.020/√417·0.02 ≈ 0.064. Joint (independent samples)
SE of the difference ≈ √(0.026² + 0.064²) ≈ 0.069; observed gap 0.12 → z ≈
1.7 — not decisive. The honest sentence: "measured betas differ at the two
horizons, but the difference is 1.7 standard errors: suggestive of
horizon structure (see module 08's lead-lag discussion), not proof." Most
desks would (wrongly) read 0.97 vs 0.85 as a fact.
</details>

## Self-grade

- Closed form for β̂ and α̂: cold?
- Can you write `ols()` from a blank cell in under 3 minutes?
- The levels-regression trap, named in one sentence?
