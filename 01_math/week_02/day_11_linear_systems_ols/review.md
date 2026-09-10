# Review — OLS Geometry

## Retrieval

1. Write the normal equations; what shape is each term?
2. What does the ones-column give you? What happens without it?
3. What does "residuals ⊥ regressors" mean, and why does it define the solution?
4. Why `solve` instead of `inv`?

<details><summary>Answers</summary>

1. $X^\top X\hat\beta = X^\top y$: k×k · k = k; left system solved, not inverted ideally.
2. An intercept; without it, the fit is forced through the origin and both
   slope and intercept are wrong.
3. The leftover is uncorrelated with the regressors — if it weren't, you
   could adjust β to reduce SSE further, contradiction with optimality.
4. Faster and numerically stabler; same answer.

</details>

## Elaboration

- Your hand-OLS matched statsmodels to 4 decimals. Explain to a skeptic why
  that means you've "earned" the black box.

## Spaced repetition

- Normal equations return in module 06 (with standard errors attached) —
  re-derive `ols_by_hand` from memory at +1 week.
