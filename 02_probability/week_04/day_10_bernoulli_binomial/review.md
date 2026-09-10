# Review — Bernoulli & Binomial

## Retrieval

1. E and Var of Bernoulli(p); of Binomial(n,p); of the estimator p̂.
2. SE(p̂) at n=63, 252, 1260 (p≈0.5) — from memory.
3. Why is p=0.5 the noisiest case? What does the parabola imply for
   evaluating high-win-rate strategies?

<details><summary>Answers</summary>

1. p, p(1−p); np, np(1−p); p(1−p)/n.
2. ≈ 0.063, 0.031, 0.014.
3. p(1−p) maximized at 0.5; high-p strategies have smaller per-trial
   variance but their *evidence about p* still scales as 1/√n.

</details>

## Elaboration

- 8 winning months of 10: compute P(≥8|p=0.5) and state the win rates
  consistent with the observation.
- Explain why comparing win rates across different trade frequencies
  without mentioning n is meaningless.

## Spaced repetition

- This is the checkpoint's engine (day 21) and module 04's multiple-testing
  engine — instant recall at +1 week.
