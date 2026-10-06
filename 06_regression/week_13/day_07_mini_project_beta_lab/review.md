# Day 7 Review — Mini-Project: Beta Lab

## Retrieval (answers)

1. Rolling β̂ closed form: rolling cov / rolling var; rolling σ̂_e² =
   σ̂_y²(1−ρ̂²) gives rolling SEs with zero regression loops.
2. Window trade-off: shorter window = responsive but noisier (SE ∝ 1/√W);
   longer = stable but stale. There is no right window, only a stated one.
3. YoY beta persistence: ranking persists (~0.5–0.8 cross-sectionally),
   levels wander — quote ranks boldly, levels with bands.
4. Overlapping-window trap: rolling estimates share W−1 of W points, so
   their wiggle CANNOT be compared to an independent-sample SE — benchmark
   on a constant-beta simulation instead.
5. "Adjusted beta" ⅔β̂ + ⅓: shrinkage toward 1, answering sampling noise
   + mean reversion (module 03's shrinkage idea, industry edition).

## Elaboration prompts

- Explain to a PM why "beta = 1.43" on a fact sheet carries less
  information than your Part 2 chart, even though both come from the same
  regression.
- Give one concrete false trading conclusion from using full-sample betas
  in a low-vol year to set hedge sizes for a high-vol year.

## Interleaved problem

Your desk's risk system uses 2-year weekly betas (W = 104 weeks) updated
monthly. A portfolio is hedged to "beta-neutral". In a crash month the
book loses 9% with the market down 12%. Autopsy the hedge: which four
beta-estimation choices could each explain part of the loss, and what
would you check for each?

<details><summary>Reference answer</summary>

(i) **Window staleness** — 2-year betas averaged the calm into the
denominator; crash betas rise (correlation spike). Check: recompute with
60-day daily betas through the crash; size the gap. (ii) **Frequency/
horizon** — weekly betas ≠ crash-horizon betas (lead-lag, beta at
different horizons differs; module 08). Check: daily horizon β̂ vs the
weekly one. (iii) **Benchmark mismatch** — hedged vs SPY while the book
is sector-concentrated; residual sector beta unhedged. Check: two-factor
(market + sector) exposure table. (iv) **Sampling error never quoted** —
the "neutral" was a point estimate ±~0.15; the loss is within the band.
Check: the rolling chart + band (your Part 2). The meta-lesson:
"beta-neutral" is a distribution, not a state; the hedge failed by the
width of its own confidence interval.
</details>

## Spaced repetition

- Rolling-beta drill (closed-form, one chart, one band): +1 month, from
  blank, on a different universe.
- The constant-beta null benchmark idea: +3 months — re-derive why naive
  wiggle-vs-SE comparison overstates time variation.

## Self-grade

- The rubric's five rows: would YOU pass your own report?
- Can you state, unprompted, the two reasons a fact-sheet beta is a weak
  input, and the one thing it is good for (ranking)?
