# Review — Portfolio Variance

## Retrieval

1. Write the two-asset variance formula; identify the diversification term.
2. Write the N-equal-weights variance formula and its limit. Say the limit in plain words.
3. Why is a dollar-neutral portfolio still risky?
4. Why does the diversification curve flatten, and what single quantity sets the floor?

<details><summary>Answers</summary>

1. $w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho\sigma_1\sigma_2$; the
   covariance (last) term is where cancellation lives.
2. $\frac{\bar\sigma^2}{N} + \frac{N-1}{N}\overline{cov} \to \overline{cov}$:
   you can diversify idiosyncratic risk, never common risk.
3. Its variance is $\mathbf{w}^\top\Sigma\mathbf{w}$ with w summing to zero —
   covariances with the *net* factor exposure remain (and the long/short
   legs each carry idiosyncratic risk).
4. Averaging kills the 1/N part; average covariance is the irreducible floor.

</details>

## Elaboration

- Explain to a colleague why crisis-correlated assets make "100 stocks ≈ the
  market" become "100 stocks = one big bet" — using the formula, not vibes.

## Spaced repetition

- THE formula of the course: re-derive at +1 week, +1 month (module 11
  depends on instant recall).
