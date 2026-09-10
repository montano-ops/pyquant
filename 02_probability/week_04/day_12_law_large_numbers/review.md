# Review — Law of Large Numbers

## Retrieval

1. The LLN statement and the SE-of-mean formula; the quadruple rule.
2. Dilution vs compensation — the gambler's fallacy corrected.
3. Roughly how many days for a 0.0005-edge, 0.011-vol strategy to clear
   2 SEs?

<details><summary>Answers</summary>

1. x̄→μ; Var(x̄)=σ²/n so SD=σ/√n; 4× data halves noise.
2. Losses are diluted by future data, never compensated — the mean
   converges, the path doesn't owe you anything.
3. SE=0.0005 needs √n = 0.011/0.0005/2 ≈ 11 → n ≈ 121×... compute: need
   2·σ/√n ≤ μ → √n ≥ 2σ/μ = 44 → n ≈ 1,936 days ≈ 7.7 years.

</details>

## Elaboration

- Vol is estimated far more precisely than the mean at the same n. Why
  (think: what's the signal-to-noise of each estimation problem)?

## Spaced repetition

- THE module number: 2σ/μ (days to t=2). Re-derive at +1 week and again
  when t-stats arrive (module 04.4).
