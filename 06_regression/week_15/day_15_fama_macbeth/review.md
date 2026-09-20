# Day 15 Review — Fama–MacBeth

## Retrieval (answers)

1. The break: pooled SEs assume cross-sectional independence; same-month
   market exposure makes corr(u_i,t, u_j,t) ≈ 0.3–0.9 → classical and
   White blind (diagonal), NW blind (wrong axis): pooled t inflates 2–5×.
2. Two steps: monthly cross-sectional OLS → λ̂_t; then mean(λ̂_t),
   SE = std(λ̂_t)/√T (+NW on the slope series if its ACF demands).
3. Conventions: cross-sectional z-scores per month (comparable λ̂_t);
   characteristics lagged beyond the return window (look-ahead defense);
   report mean / SE / t / share_pos / mean monthly R².
4. Tournament number: pooled classical on a persistent-characteristic
   panel null rejects ~35–40% at 5% nominal; FM ≈ 5%. (Fresh-monthly
   characteristics mostly escape — persistence is the mechanism.)
5. Time-series slope prices variation within a name; cross-sectional
   slope prices exposure across names. FF92 = cross-sectional.

## Elaboration prompts

- FM is "cluster-robust by design". Explain which dependence it sidesteps
  and which one remains on the table (the λ̂_t ACF), with the repair.
- Why is the FM premium the same number as the pooled premium so often —
  and why does that make the SE mistake MORE dangerous, not less?

## Interleaved problem

A study reports FM slopes with SE = std(λ̂_t)/√T, T = 360 months:
λ_size = −0.15%/σ (t = −3.2). You notice λ̂_t's lag-1 ACF is 0.42 (size
premium is regime-persistent). (a) What is wrong with the quoted t and
which single-tool repair applies? (b) Roughly how much does the t shrink?
(c) Why did nobody need this correction in E3's tournament world?

<details><summary>Reference answer</summary>

(a) std/√T assumes the λ̂_t draws are uncorrelated; ACF 0.42 means the
effective count is well below 360 — apply Newey–West to the λ̂_t series
(intercept regression, HAC meat, L ≥ the ACF tail ≈ 6–12 months). (b) The
HAC-inflation factor ≈ √((1+ρ)/(1−ρ)) ≈ √(1.42/0.58) ≈ 1.6× on the SE for
an AR(1)-flavored slope series — t −3.2 becomes ≈ −2 — still honest, but
the margin mattered; (c) E3's null world had fresh-monthly z and white
noise slopes by construction (ρ ≈ 0), so std/√T was already exact. Rule:
FM step 2 always ships with the λ̂_t ACF printed, the way day 10's page
ships with the demands list.
</details>

## Spaced repetition

- fama_macbeth() from blank + fm_table rows: +1 week.
- Pooled-vs-FM tournament result: +1 month, re-derive the inflation
  formula √(1+(N−1)ρ̄).
- The ACF-on-slopes check: permanent habit, every FM table.

## Self-grade

- Can you state the two-step with both formulas cold?
- E1's arithmetic: could you redo it on a napkin with new numbers?
- The interpretation pair (variation vs exposure): fluent?
