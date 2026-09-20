# Day 17 Review — Rolling & Expanding Windows

## Retrieval (answers)

1. Rolling: last W points only — faith: world drifts; pays variance
   (SE ≈ σ_e/σ_x√W). Expanding: all points — faith: world stable; pays
   staleness.
2. Constant-world wander: rolling estimates of a constant parameter
   wander within ~±2·SE(W); W = 252 ≈ ±0.1–0.2 for market betas — the
   band is the difference between drift and noise.
3. Adjacent-window overlap: ACF(W−l)/W; a single event looks like a
   W-length "regime". Inference about changes uses disjoint splits or
   pre-declared interactions, not rolling-to-rolling comparisons.
4. Informal Chow: z = (β̂₁−β̂₂)/√(SE₁²+SE₂²) on disjoint subsamples;
   split declared by calendar ex-ante.
5. Calibration: W = 63 rumor (SE≈0.13); 252 quotable-with-band (≈0.06);
   1008 stable-but-stale (≈0.03) for σ_e≈σ_x.

## Elaboration prompts

- "The band is what separates estimation from history." Explain to a PM
  using the E2 table.
- Why does an expanding window fail *gracefully* (bias, slow) while a
  short rolling window fails *loudly* (variance, fast)? Which failure
  mode is more dangerous for a slow-moving risk committee?

## Interleaved problem

Your factor's rolling 36m premium λ̂ (day-15 FM) trends down for five
years: 8bp/σ → 1bp/σ. Three rival readings: (i) the premium is dying;
(ii) estimation noise; (iii) one 2020 event sliding through windows.
Write the test for each and the honest interim sentence.

<details><summary>Reference answer</summary>

(i) Premium decay: fit λ̂_t ~ time trend with HAC SEs (the λ̂_t series is
autocorrelated — day 15's check), and require the trend to survive
re-estimation on annual non-overlapped λ̂'s; (ii) Noise: the wandering
band around a CONSTANT premium is ±2·std(λ̂_t)≈±2·SE·√T behavior — compare
the observed 5-year trend to constant-premium simulations of the same
FM pipeline (E2's constant-world wander, panel edition); (iii) Event
contamination: inspect λ̂_t minus its 2020 months; a spike-insensitive
trend survives their deletion. Interim sentence: "the premium's rolling
estimate declined 8→1bp over five years; split-sample and HAC-trend tests
are consistent with either a slow decay or a 2020-event-driven window
shadow; we treat the premium as reduced but not dead, pending next
year's out-of-window data." — honest, falsifiable, dated.
</details>

## Spaced repetition

- E2 table (W vs observed range vs band): +1 month, regenerated from
  blank with a different seed.
- The three admissible time-variation claims: +3 months, dictated cold.

## Self-grade

- The two schemes with their faiths, cold?
- The wander band arithmetic (4·SE(W)) mental-math ready?
- E5's production answer: could you deliver it as spoken, not read?
