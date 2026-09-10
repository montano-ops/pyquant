# Review — Expectation & Variance

## Retrieval

1. E[X] and Var(X) for a win/lose (p, W, L) bet.
2. State linearity of expectation and the portfolio consequence.
3. The three-layer stack — which layer holds biases?

<details><summary>Answers</summary>

1. E = pW − (1−p)L; Var = p(1−p)(W+L)².
2. E[aX+bY] = aE[X]+bE[Y] → portfolio expected return is the weighted
   dot product w·μ.
3. Layer 1 = truth (never seen); layer 2 = sample statistics (noisy);
   layer 3 = the one realized path (bias lives here: survivorship,
   look-ahead, selection).

</details>

## Elaboration

- Explain "E[X] is not a promise" using μ=0.04%, σ=1.1% and the
  signal-to-noise ratio μ/σ (the embryo Sharpe).

## Spaced repetition

- This is the module's hinge day: revisit at +1 week (day 12 uses it),
  and again when Sharpe is formalized (module 12.15).
