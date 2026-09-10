# Day 3 Review — Hypothesis Testing

## Retrieval (answers)

1. H₀ = the kill (no effect; assumed); reject when data are rare under
   it; never "accept." Asymmetric by design.
2. p-value = P(data ≥ this extreme | H₀). NOT P(H₀ | data); NOT "the
   chance the result is luck" (needs a base rate).
3. p uniform under H₀ → 100 null tests ≈ 5 discoveries; P(≥1) ≈ 99.4%.
4. One-sided = pre-committed direction only; choosing after seeing the
   sign halves p fraudulently.
5. The significance dance: p is itself a statistic with a sampling
   distribution; a true effect near the boundary crosses the line
   repeatedly.
6. The five paper questions: what H₀, what statistic/SE, which side,
   what power, how many siblings.

## Elaboration prompts

- Watch the dance yourself: simulate a true SR-0.4 strategy, plot its
  rolling 2-year p-value for 10 years. Count the crossings of 0.05.
  Write the sentence you'd send the PM who panicked at the second
  crossing.
- The five paper questions, applied to a paper you know (or JT93):
  answer all five for one results table.

## Interleaved problem

A quant shows a 3-month backtest: t = 2.3, p = 0.021, two-sided, of 40
signals tested in the same session. (a) Expected significant results
under all-null? (b) The Bonferroni-adjusted p (preview)? (c) The
Bayes-discounted P(real) with a 1-in-10 base rate and power 40%?

<details><summary>Reference answer</summary>

(a) 40 × 0.05 = 2 — two "discoveries" expected from pure noise; his
one is unremarkable in context. (b) 40 × 0.021 = 0.84 — not
significant after the preview correction (week 9 does this properly).
(c) (0.1×0.4)/(0.1×0.4 + 0.9×0.05) = 0.04/0.085 ≈ 47% — a coin flip,
even with a generous base rate. **Three tools, same verdict: a
selected t-statistic from a batch is not evidence until the batch is
priced in.**
</details>

## Self-grade

- p-value definition: verbatim, cold?
- The 5%-lottery simulation: run from scratch in under 2 minutes?
