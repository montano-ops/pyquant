# Review — Week 5 + Module 02 Integration

## Cold retrieval (the module's spine, one page, from memory)

1. E/Var → Var(aX+bY) → portfolio variance → SE of mean → CLT →
   t-statistic shape: write the chain.
2. The two anchor simulations (SE(p̂) table; best-of-500 noise) —
   reproduce or die.
3. The shuffle argument in five sentences.

<details><summary>Self-grade</summary>

The chain is the module. If any link is missing, that link's day gets
redone *before* the checkpoint — the checkpoint tests the chain, not the
links in isolation.

</details>

## Mixed problems (interleaved, exam-style)

1. Binomial: P(≥138/252 | p=0.5) — exact and by normal approx.
2. Correlation: ρ̂=0.35 over 126 days — z vs 0? Consistent with 0.1?
3. Bayes: 1% base rate, 90% hit, 20% false alarm → posterior?
4. LLN: how many days to resolve a 0.0003 edge at 0.012 vol to t=2?
5. Design: a placebo test for "5-day momentum adds value" — what do you
   shuffle, what must you preserve?

<details><summary>Answers</summary>

1. z = (0.548−0.5)/√(0.25/252) ≈ 1.51 → normal one-sided ≈ 0.065; exact
   binomial ≈ 0.074 (the continuity correction closes the gap).
2. SE ≈ 1/√126 ≈ 0.089 → z ≈ 3.9?? — careful: SE(ρ̂) under ρ=0 is
   (1−ρ̂²)/√T ≈ 0.088 → z ≈ 4.0 vs 0; vs 0.1: z ≈ 2.8 — distinguishable
   from both.
3. (0.9×0.01)/(0.9×0.01+0.2×0.99) = 0.009/0.207 ≈ 4.3%.
4. n = (2σ/μ)² = (2×0.012/0.0003)² = 80² = 6,400 days ≈ 25 years.
5. Shuffle signal dates jointly with... no — destroy signal-return
   alignment *within* blocks: circular-block-shift the signal relative to
   returns, preserving each series' own structure.

</details>

## Systems check

- [ ] PROGRESS.md: module 02 days 1–20 ticked with minutes.
- [ ] All module-02 concepts added to spaced schedule (expectancy, SE
      tables, Bayes, CLT caveats, shuffle principle).
- [ ] Tomorrow: the checkpoint memo is the deliverable — sleep first.
