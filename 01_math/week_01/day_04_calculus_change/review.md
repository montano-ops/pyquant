# Review — Calculus I: Change

## Retrieval

1. Define the derivative as a "nudge ratio" in words and in formula.
2. Name four finance aliases for derivatives.
3. What is convexity, and why does it make −50%/+100% end flat rather than up?
4. Why is h = 10⁻¹⁶ a bad choice for a finite difference?

<details><summary>Answers</summary>

1. Nudge x by h, measure Δy, take the ratio, shrink h:
   $f'(x)=\lim_{h\to0}[f(x+h)-f(x)]/h$.
2. beta, delta, duration, gradient, marginal P&L.
3. Second derivative > 0 — curvature. The path loses half then gains half
   back of a *different base*: 0.5 × 1.5 = 0.75? no — 0.5 then ×1.5... the
   point: multiplication isn't symmetric around losses; compounding is
   convex in log space.
4. Floating-point cancellation: f(x+h) − f(x) loses all significant digits.

</details>

## Elaboration

- "A hedged position is linear; an insured position is convex." Explain the
  difference and what each costs you per day (preview of module 15).

## Spaced repetition

- Finite differences return as the Greeks (module 15) — re-derive `deriv()`
  from memory at +1 month.
