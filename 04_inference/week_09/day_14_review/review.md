# Day 14 Review — Week 9 Review

## Retrieval (answers)

1. Welch df: (a+b)²/(a²/(n₁−1) + b²/(n₂−1)), a = s₁²/n₁, b = s₂²/n₂.
2. Paired SE > Welch SE when the two series are negatively
   correlated (equity vs bonds): the covariance term *adds* variance
   to the difference.
3. Bootstrap resamples *values* (sample ≈ population) → sampling
   distribution; block length keeps dependence of length ≤ b.
   Permutation shuffles *labels* → null distribution; naive shuffle
   forbidden on time series (destroys the dependence being tested).
4. m = 100 at 5%: E[V] = 5; P(V ≥ 1) ≈ 0.994.
5. BH: largest k with p(k) ≤ kq/m; reject the k smallest.
6. Junk fraction is set by family size m (the zoo arithmetic), not
   the statistic — hence t > 3 as m grows.
7. H1 Monday ≠ 0; H2 Monday ≠ other 4 days (the tradable contrast);
   H3 some day is special (the family).
8. ρ_k = (H−k)/H, k < H; Bartlett factor √H; corrected t = naive/√H;
   Monte-Carlo proof: naive rejects ~30%, corrected ~5% on null.

## The week's spine

> Every claim in research is (estimate, SE, family size). The SE has a
> design; the family has a count. A number without both is a lottery
> ticket.

## Error log

The deliverable. Format per miss: what I thought → what was true →
why. Review it again on day 04.18.

## Spaced-repetition schedule (set your dates)

- **Next review day (04.18):** Welch df, BH rule, Bartlett factor,
  the spine sentence — from memory.
- **One month:** re-run day 04.13 E2 (Monte-Carlo proof) unaided.
- **Three months:** the 04.12 E5 mini-report, from scratch, new asset.

## Self-grade

- Did you complete the retrieval block with zero notes and ≤ 20 minutes?
- Are all misses in the error log with the *why*?
- Can you state the spine sentence without hesitation?
