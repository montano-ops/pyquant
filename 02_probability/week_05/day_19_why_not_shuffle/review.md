# Review — Why Not Shuffle

## Retrieval

1. What does shuffling preserve/destroy — and which null does it test?
2. The placebo design principle.
3. Block bootstrap in one sentence; the n_eff formula intuition.

<details><summary>Answers</summary>

1. Preserves the marginal distribution (same returns!), destroys order →
   kills vol clustering and all path statistics; tests the marginal null,
   not the time-series null.
2. Destroy exactly the tested structure, preserve everything else.
3. Resample contiguous blocks (length ≥ dependence horizon) with
   replacement; dependence inflates mean-variance by 1+2Σρ_k → n_eff < n.

</details>

## Elaboration

- A vol-targeted strategy evaluated with a shuffle placebo: does the
  placebo over- or under-state the real sampling noise? Why?

## Spaced repetition

- Placebo design day is module 13.17; purged CV is 13.9. This principle
  is permanent equipment — restate it at +1 month.
