# Day 2 Review — Confidence Intervals

## Retrieval (answers)

1. Correct read: the *procedure* covers μ in 95% of samples; this
   interval is in or out, no probability left. Wrong reads: "95%
   probability μ is inside" (parameter not random); "95% of returns
   fall here" (prediction interval — ~100× wider at daily scale).
2. Coverage simulation: ~95% under normal parents; fat tails + small n
   sag it toward 92–94%.
3. SPY 15-year annualized mean CI: roughly [1%, 14%] — the honest
   uncertainty in "expected return" from a decade and a half.
4. CI ↔ test duality: the 95% CI is the set of μ₀ a 5% two-sided test
   would not reject.
5. Sharpe CI at 1 year ≈ ±1 (annualized units) — one-year Sharpes are
   nearly uninformative.

## Elaboration prompts

- Find a real allocation memo/factsheet quoting a point expected
  return. Write the CI they should have printed, using the arithmetic
  from §3 (any 10–15y window, σ≈15–20% annual).
- The prediction-interval confusion: draft the two-sentence disclaimer
  that keeps "0.04% ± 0.02% daily" from being read as a loss bound.

## Interleaved problem

A strategy's daily mean: +0.031%, SD 0.9%, n = 1,260 (5 years).
(a) 95% CI. (b) Annualized. (c) Is 8%/yr a defensible marketing claim?
(d) What n would halve the CI width?

<details><summary>Reference answer</summary>

(a) SE = 0.9%/√1260 ≈ 0.0254%; CI = 0.031% ± 0.050% = [−0.019%,
+0.081%] daily — straddles zero. (b) ×252: [−4.8%, +20.4%] — the
annualized CI is grotesquely wide (compounding skews it; the linear
scaling is an approximation — note that in real work you'd bootstrap
the annual). (c) 8%/yr sits comfortably inside [−5%, +20%]: the claim
is *consistent* with the data and equally consistent with zero —
"defensible" only with the band printed next to it. (d) Width ∝ 1/√n:
need 4× the data = 20 years. Halving uncertainty costs 15 years —
the (2σ/μ)² law in CI clothing.
</details>

## Self-grade

- The procedure-vs-probability read: can you state it cold, in one
  sentence, without hedging?
- Did you run the coverage simulation yourself, including the fat-tail
  version?
