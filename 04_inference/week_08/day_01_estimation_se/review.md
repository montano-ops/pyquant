# Day 1 Review — Estimation & Standard Error

## Retrieval (answers)

1. Consistency (→θ as n→∞), unbiasedness (E[x̂]=θ at any n),
   efficiency (least variance). MSE = bias² + variance licenses
   deliberate bias (shrinkage) but never unknown bias.
2. Paired SE = SD(difference)/√n — the shared market cancels;
   independent formula ignores the cancellation and overstates.
   Typically the paired SE is far smaller.
3. Three violations: fat tails (small-n SEs of means understated;
   t runs hot), vol clustering (n_eff < n; SE × √(n/n_eff)),
   non-stationarity (the parameter moves; no SE fixes the question).
4. t ≈ estimate/SE — "how many SEs from zero" — the lens for every
   table in every paper.

## Elaboration prompts

- Write the SE-floor paragraph for your own strategy's backtest: which
  of the three violations applies, in which direction, roughly how
  big? (If clustering: compute the ACF of |r| → n_eff and multiply.)
- Why is "the estimator is unbiased" cold comfort at n=252 for a
  mean-return question? (Unbiased describes the long run; your SE says
  the long run is decades away.)

## Interleaved problem

Strategy A and benchmark B, same 1,000 days. SD(A) = 1.2%, SD(B) =
1.1%, corr(A,B) = 0.85. (a) SD of the active return A−B? (b) SE of the
mean active return vs the independent-formula SE? (c) The active
return's mean is 4bp — t-stat, paired?

<details><summary>Reference answer</summary>

(a) Var(A−B) = sA² + sB² − 2·0.85·sA·sB = 1.44 + 1.21 − 2.245 =
0.405 → SD ≈ 0.64%. (b) SE_paired = 0.64%/√1000 ≈ 2.0bp;
SE_independent = √(1.44+1.21)/√1000 ≈ 1.63%/31.6 ≈ 5.2bp — 2.6× too
big. (c) t = 4/2.0 = 2.0 — borderline significant, honestly computed.
With the independent SE it would be 0.8 — invisible. **Pairing IS the
difference between a hedge-fund result and a null one; active-return
evaluation is always paired.**
</details>

## Self-grade

- Can you produce the difference-of-means SE table row from memory,
  both versions?
- Did you compute an n_eff for anything you actually trade/care about?
