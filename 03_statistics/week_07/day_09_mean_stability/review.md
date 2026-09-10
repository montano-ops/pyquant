# Day 9 Review — Is the Mean Stable?

## Retrieval (answers)

1. Rolling 63d mean of SPY: roughly −0.10%/day to +0.15%/day; below
   zero 25–40% of days. Under a CONSTANT μ = 0.04% with SE ≈ 0.13%,
   that's exactly what noise alone produces (P(z<0) ≈ 49%... for the
   full distribution, swings of ±2 SE ≈ ±0.26% — the observed range
   is consistent with pure noise).
2. Three explanations: pure noise (constant μ, sampling wobble); regime
   drift (μ really differs by era); time-varying risk premium (μ_t
   moves with vol/rates/sentiment).
3. Chunk-spread test: compare observed spread of sub-period means vs
   each chunk's SE — observed 1.5–2.5× SE suggests drift but overlaps
   with noise at these n's.
4. The equity premium over 30-year windows: historically ~2–9%/yr
   depending on start date — the "mean" is a distribution.
5. The asymmetry: drift unstable AND unpredictable; vol unstable BUT
   predictable. This organizes modules 09–11.

## Elaboration prompts

- Your strategy's edge: what window would you need to detect a 50%
   decay in it? (Reuse module 02.12's n = (2σ/Δμ)² with today's
  honesty: if the answer is "more data than exists," the edge is
  unmonitorable in real time — design for that.)
- "The mean is a moving target" — write the two-sentence risk
  disclosure for a product whose marketing assumes a fixed mean.

## Interleaved problem

Fund A: 2010–2015 mean 0.09%/day; 2016–2021 mean 0.02%/day. Daily σ =
1.1% throughout, n ≈ 1260 per half. Is the "decay" statistically real?
What sample would settle it?

<details><summary>Reference answer</summary>

Difference 0.07%/day; SE of each half's mean = 1.1%/√1260 ≈ 0.031%; SE
of the difference ≈ 0.044%. t = 0.07/0.044 ≈ 1.6 — under 2: NOT
established at conventional thresholds. It *looks* like a decay (one
eras's luck?) but is within noise. To settle at 2 SE you'd need the
difference's SE ≤ 0.035% → each half needs n ≈ (1.1/0.035)² ≈ 990...
wait, compute: SE_diff = 1.1%·√(2/n) = 0.035% → n ≈ 2·(1.1/0.035)² ≈
1,980 days per half — about 8 years each, and *that* assumes the mean
is constant within each half (it isn't; drift-within-drift defeats
precision). The deeper answer: strategy means are barely monitorable —
which is why process (execution quality, crowding measures) must
substitute for outcome monitoring. Note also the selection caveat: you
*noticed* the decay because it looked like a decay — the test is
post-hoc (module 04's peeking problem).
</details>

## Self-grade

- Could you derive "49% below zero under constant μ" yourself?
- The drift-vs-risk predictability asymmetry: can you state it cold,
  with the evidence for each half?
