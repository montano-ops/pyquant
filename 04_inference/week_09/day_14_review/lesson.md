# Day 14 — Review (Week 9)

## How to use today

No notes for the retrieval block — that is the point. Time yourself:
each item in 2 minutes. Then run the mixed problem set (exercise
notebook) before looking at the solution. The error log is the
deliverable: every miss goes in, with the *why*.

## Retrieval (no notes — 2 min each)

1. Welch df formula, from memory.
2. When is the paired SE *larger* than the Welch SE?
3. Bootstrap: what is resampled, what is estimated, and the block
   length's job.
4. Permutation: what is shuffled, what null it builds, and why naive
   shuffling is forbidden on time series.
5. m null tests at 5%: E[V] and P(V ≥ 1), for m = 100.
6. BH: the rejection rule in one line.
7. The zoo calculation: what sets the junk fraction (not the
   statistic).
8. The three conflated day-of-week claims (H1/H2/H3).
9. Overlapping H-day ACF triangle and the Bartlett factor.
10. Monte-Carlo signature that proves a correction works.

## The week's spine (if you can say this, the week worked)

> Every claim in research is (estimate, SE, family size). The SE has a
> *design* (paired? overlapping? clustered?) and the family has a
> *count* (how many tests, which ones). A number without its design
> and its family is not a result — it is a lottery ticket.

The three resampling tools are the same skeleton: draw fake data from
a stated null/assumption, measure how the statistic moves, read the
probability. Bootstrap: sample ≈ population → sampling distribution.
Permutation: labels arbitrary → null distribution. Block: the time
structure gets a length-b allowance in both.

## What to schedule (spaced repetition)

- **Next week (review day 04.18):** Welch df, BH rule, Bartlett
  factor, the (estimate, SE, family) sentence — from memory.
- **One month (around day 06.18 "which SE when"):** re-run E2 of
  day 04.13 (the Monte-Carlo proof) without looking at the solution.
- **Three months:** the weekend-effect mini-report (04.12 E5) from
  scratch on a new asset.

## Error log

For every retrieval item you missed and every mixed problem you got
wrong: what you thought, what was true, why the mistake happened.
This is the week's real deliverable.
