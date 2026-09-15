# Day 20 — The Mixed Problem Set

## How to use today

Six problems, in increasing difficulty, each one a piece of the
checkpoint audit. No notes for the first pass; time yourself
(~15–20 minutes each). The solution walks each one in the
researcher's voice — read it for the *structure* of the answer, not
just the numbers.

## The problems

**P1 (L4) — The paired audit.** Two strategies, 800 days, same
dates: SDs 1.4% and 1.1%, correlation 0.72, means 3.1bp and 1.9bp.
Which design? The t? The paired SE in the first line of the answer?

**P2 (L5) — The bootstrap that must match.** A 2,000-day return
series: the mean's bootstrap SE (B = 5,000) vs s/√n vs the
clustering-adjusted s/√n_eff (|r|-ACF rule). All three, one table;
explain the spread.

**P3 (L5) — The permutation on the right null.** Two assets, 3,000
days, corr = −0.28. Permutation p for "corr = 0" (shuffle one
series, B = 2,000) vs Fisher-z p. Why are they close here — and on
what data would the permutation version be *wrong*?

**P4 (L5) — The screen.** 80 candidate characteristics, 1,000
stock-months each, monthly. How many |t| > 2 by noise? Run BH at
q = 0.05 on a simulated pure-noise screen: how many "survive," and
what is their honest composition?

**P5 (L5) — The overlapping audit.** H = 21, N = 1,800, mean 6bp,
SD 28bp. Naive t; Bartlett factor from the ACF; corrected t;
non-overlapping equivalent (N, t). Show the two designs agree.

**P6 (L7) — The full audit (the checkpoint preview).** A paper:
"characteristic Z (top quintile vs bottom quintile, quarterly,
non-overlapping): +1.1%/yr, t = 2.7, n = 72 quarters, family of 9
tested, 12bp round-trip cost at intended size, vol 18%/yr."
Write the complete verdict: grill (four questions), gate, and the
one-paragraph disposition.

## The self-check (end of day)

1. Which of P1–P6 would you redo *without* the solution and still
   get right? Be honest — the answer is your checkpoint readiness.
2. The slowest problem: what made it slow (arithmetic? structure?
   which tool was fuzzy)?
3. One sentence on the module you're leaving: the one habit you
   actually installed.

---

**Answers:** see solution.ipynb (worked, in the researcher's voice).
The structure you should recognize in every answer: *state the
design, compute the honest number, count the family, price the
cost, give the conditional verdict.*
