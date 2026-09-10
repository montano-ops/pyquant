# Day 6 Review — Week-8 Consolidation

## Cold retrieval (reference answers)

1. Estimator trio + MSE ledger; deliberate bias OK (shrinkage),
   unknown bias never.
2. Paired difference SE = SD(A−B)/√n; the market cancels; active
   return evaluation is always paired.
3. SE floors: fat tails (t hot at small n), clustering (n_eff),
   non-stationarity (question misspecified).
4. CI: procedure covers 95%; this one is in-or-out; duality with the
   5% test; prediction interval ≠ CI (~100× at daily scale).
5. p = P(data|H₀); uniform under H₀; one-sided needs pre-commitment;
   the dance is the p-value's own sampling noise.
6. t = SR·√Y; (2/SR)² years to t=2; implied-SR reading of papers.
7. Three breaks: fat tails (+1.5–2× p at n=60), clustering (SE ×
   √(n/n_eff)), overlap/autocorrelation (worst; HAC in week 9).
8. 2×2; power curves; the design equation; dead designs.
9. Statistical / economic / tradable — three independent answers.
10. Posterior discounts: 80%/50%/14% at base rates 1/5, 1/20, 1/100.

## Interleaved problems (reference answers)

**P1.** t_A = 0.8·√3 = 1.39; t_B = 0.4·√12 = 1.39 — identical t!
Trust: B (longer, more information per unit noise) — but note t alone
cannot distinguish them; the same t from more years implies a *lower*
Sharpe with tighter CI. Two questions: "how strong is the evidence"
(t — tied) vs "what do we know about the strategy" (B, less variance
around a smaller claim).

**P2.** (a) Excludes 0 → reject at 5%. (b) Net = 2bp upper bound vs
25bp costs → dead at the CI's top end. (c) No sample settles a
*cost* question — the economic verdict needs the cost number, not
more data; more data only tightens [2, 38].

**P3.** Expected significant under all-null: 200 × 0.05 = 10 —
observed 14 is barely above the noise casino's house rate. Minimal
honest correction: report expected-luck alongside (or BH/Bonferroni,
week 9); the 8 funded need power + economic screens, not
significance.

**P4.** Overlap/autocorrelation: biggest, possibly halving effective
n → t 2.1 → ~1.5; fat tails at n=48: +~1.5× on p (0.049 → 0.07-0.08);
multiplicity: if one of many tried signals, p is the price of the
search, not the signal.

**P5.** "Accept" requires proving a negative; power quantifies what
you CAN'T see; significance tracks n, effect size doesn't — a
t-statistic is an effect size wearing an n-costume (divide by √Y to
undress it).

## Build check

The 15-minute inference report (mean, SE, CI, t, p, implied SR,
years-to-t=2, with the three-break caveat note): cold? That's
tomorrow's lab instrument, and module 05's day-1 tool.
