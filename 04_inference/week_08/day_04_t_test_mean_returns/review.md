# Day 4 Review — The t-Test for Mean Returns

## Retrieval (answers)

1. t = x̄/(s/√n) ~ t(n−1) under iid normal-ish; = SR_annual·√years.
2. Years to t=2: Y = (2/SR)² — SR 1.0→4y, 0.7→8y, 0.5→16y, 0.3→44y;
  80% power (one-sided): 6/13/25/69 years.
3. Reading a paper's t: divide by √Y → implied Sharpe → plausible? →
   mined? (multiplicity context).
4. Three breaks: fat tails (n=60 nominal 5% → 6–8% actual; repaired by
   CLT at n≳500), vol clustering (SE understated √(n/n_eff)),
   serial correlation/overlapping (SE inflated badly — HAC, day 13).
5. Checklist: n/frequency, parent kurtosis, autocorrelation, sibling
   count, implied SR.

## Elaboration prompts

- Take any three t-stats from a paper you have access to (or JT93's
  Table 1): compute implied Sharpe and years; rank by credibility
  before any multiplicity argument. What does the ranking reveal?
- Your own live/backtest strategy: compute its t honestly (paired if
  vs benchmark), then re-compute with a clustering correction
  (|r|-ACF → n_eff). How much did it move? That move is the honesty
  gap.

## Interleaved problem

Momentum WML, monthly, 1965–2025 (60 years): mean 0.72%/mo, SD
2.9%/mo. (a) t-stat. (b) Implied annualized Sharpe. (c) The 2009 crash
(−80% in 3 months) is dropped: mean falls to 0.61% — new t? (d) What
does (c) tell you about t-stats on fat-tailed spreads?

<details><summary>Reference answer</summary>

(a) SR_m = 0.72/2.9 ≈ 0.248 → t = 0.248·√60 ≈ 1.92 (two-sided p ≈
0.06 — the canonical momentum result is *barely* significant over the
full modern history at monthly frequency; the original window was
friendlier). (b) 0.248·√12 ≈ 0.86 annualized — a very strong Sharpe
for a factor spread, which is why momentum is famous. (c) New SR_m =
0.61/2.9 ≈ 0.21 → t ≈ 1.63 — dropping ONE quarter of 240 moves the
t-stat by 0.3, i.e., ~15% of the evidence lives in 1% of the sample.
(d) t-stats on fat-tailed, skewed spreads are hostage to their extreme
quarters — the SE assumes the tails are typical; winsorizing or robust
t (or reporting with/without the crash) is mandatory honesty, and the
crash sensitivity itself is the finding (momentum crash literature,
module 07).
</details>

## Self-grade

- t = SR√Y: cold, with the years-to-t=2 table?
- The three breaks, each with its direction and rough size?
