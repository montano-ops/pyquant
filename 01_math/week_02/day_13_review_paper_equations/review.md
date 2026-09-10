# Review — Decoding Paper Equations

## Retrieval (the five-step method, cold)

1. The five steps of decoding an equation?
2. Decode: $\hat\beta_i = \frac{\text{Cov}(R_i,R_m)}{\text{Var}(R_m)}$ — objects, operations, words, loop, dimensions.
3. Why do overlapping portfolios (JT93) create serially correlated strategy
   returns even if monthly returns are independent?

<details><summary>Answers</summary>

1. Objects → operations → words (no symbols) → loop/pseudocode → dimension check.
2. Objects: two return series. Operations: covariance over variance. Words:
   "the share of the market's risk that asset i co-moves with" = the OLS
   slope of i on m. Loop: accumulate products of deviations, divide. Dim: (return²)/(return²) = unitless.
3. Each month's reported return averages portfolios formed at different
   dates — adjacent months share J−1 of those portfolios, so their returns
   share almost all their randomness → autocorrelation by construction
   (HAC standard errors are the fix, module 06).

</details>

## Elaboration

- Pick any equation from a paper you have access to and run the five steps
  in writing. This is the module's real exam.

## Spaced repetition

- The five-step method is permanent equipment; re-apply to a new equation at
  +1 month (module 06's Fama-MacBeth is a good target).
