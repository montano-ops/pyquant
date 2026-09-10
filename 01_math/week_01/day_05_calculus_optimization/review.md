# Review — Calculus II: Optimization

## Retrieval

1. Write SSE(a, b) in Σ notation.
2. What two things does `minimize` need from you, and what two things must you check in its result?
3. Why does a convex objective make your life easy? Which course models are NOT convex?
4. Why squared errors — three reasons?

<details><summary>Answers</summary>

1. $\sum_{t}(y_t - a - b x_t)^2$.
2. Objective + starting point; check `res.success` and stability across starts.
3. Unique global minimum — start point doesn't matter. Non-convex: GARCH
   likelihoods, neural networks.
4. Positive (no cancellation), differentiable, penalizes large misses
   quadratically (+ makes the math linear).

</details>

## Elaboration

- An optimizer returns weights that differ wildly across starting points.
  What does that tell you about the *research conclusion*, not just the math?

## Spaced repetition

- SSE returns tomorrow (toolkit tests), then module 06 (OLS standard errors
  are curvature-of-SSE statements). Re-derive at +1 week.
