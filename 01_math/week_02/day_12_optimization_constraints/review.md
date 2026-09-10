# Review — Constrained Optimization

## Retrieval

1. Write the constrained min-variance problem (objective + two constraints).
2. What does "the constraint is binding" mean, and why does binding change the solution structurally?
3. Three craft habits when using `minimize` for portfolios?
4. Why does optimization amplify estimation error?

<details><summary>Answers</summary>

1. $\min_w w^\top\Sigma w$ s.t. $\sum w_i = 1$, $w_i \ge 0$ (say).
2. The unconstrained optimum violates it; the constrained optimum sits on
   the fence — different active set, different portfolio, not a nudge.
3. Feasible start (equal weights); assert `res.success`; re-verify
   constraints yourself.
4. The optimizer deliberately loads onto whatever entries of Σ *look*
   best — and "looks best" includes estimation luck.

</details>

## Elaboration

- Your Part-3 result (A-weights worse than 1/N on half B) is one sample.
  Why does that NOT establish "1/N always wins"? What would module 13's
  version of this test look like?

## Spaced repetition

- Returns in module 11 (DeMiguel et al.); re-run your three-regime
  comparison at +1 month.
