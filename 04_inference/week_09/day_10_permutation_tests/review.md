# Day 10 Review — Permutation Tests

## Retrieval (answers)

1. Permutation shuffles *labels* (group assignments) → estimates the
   statistic's distribution under the sharp null. Bootstrap resamples
   *values* → estimates the sampling distribution under
   "sample ≈ population."
2. p = (#{|t*| ≥ |t_obs|} + 1)/(B+1). You can only *claim* p < 1/B;
   large p's are accurate, tiny p's are bounded below by Monte-Carlo
   resolution.
3. Naive shuffling of a time series destroys the dependence the
   statistic depends on → null world too quiet → statistic looks too
   extreme → p understated → false confidence. Block permutation (b
   past the dependence horizon) is the repair.
4. Permutation needs exchangeability of labels under H₀. Before/after
   an event is not exchangeable — the honest null there is "non-event
   days are exchangeable with each other," i.e., the placebo-event
   design.
5. Validating the engine: (a) matches Welch on well-behaved data,
   (b) uniform p under the null, (c) power above 5% at a detectable
   shift.

## Elaboration prompts

- Explain "it doesn't matter which observation gets the label" to a
  colleague, in ≤ 3 sentences, for the question "does momentum sort
  future returns?"
- A paper's event study reports t = 2.3 with "standard errors
  clustered at the firm level" but no placebo days. What is missing,
  and what question does the permutation version answer that the t
  does not?
- Why can the block-permutation p be *larger* than the naive-shuffle
  p even though both are "shuffling"? (The block null is more
  realistic — it contains clustered null worlds, so the observed
  statistic is less extreme relative to it.)

## Interleaved problem

1,200 daily returns of one asset. ρ₁(|r|) = 0.22. A naive-shuffle
test of "positive autocorrelation in |r|" gives p = 0.0005.
(a) State the null the naive test actually built. (b) Why is p =
0.0005 not trustworthy here (direction + rough mechanism)? (c) What
block length would you try, and what result would change your mind
about the clustering being "real in this sample"?

<details><summary>Reference answer</summary>

(a) "|r| is a set of exchangeable numbers" — i.e., a world with the
same marginal distribution but *no temporal structure at all* (no
clustering, no level persistence). (b) The real data have clustering;
the naive null has none; positive autocorrelation is *built into the
data-generation*, so it looks extreme against a structureless null —
p understated, likely dramatically (the block p would be larger,
though often still small). (c) b ≈ 20–60 (past the clustering decay);
if the block p stays near 0 the clustering is a robust sample fact;
if it jumps to 0.1–0.4, the naive test's significance was mostly an
artifact of the test, not the data — and you'd stop calling the
clustering "strong" in this sample.
</details>

## Self-grade

- Can you state the permutation/bootstrap contrast in two sentences?
- Did you run naive vs block and *interpret the gap*, not just report it?
- Can you write the (count+1)/(B+1) correction and say why?
