# Day 5 Review — Errors, Power, Effect Size

## Retrieval (answers)

1. 2×2: α = P(Type I) — chosen; power = 1−P(Type II) — computed
   (and usually isn't, by anyone, ever).
2. Power = Φ(SR√Y − z_crit) + small left tail; SR 0.5, two-sided 5%:
   ~11% at 1y, ~30% at 5y, ~50% at 10y, ~80% at 25y.
3. The trio: estimate ± SE; significance; effect size in bp/yr vs
   costs. Three-way verdict: statistical / economic / tradable —
   independent answers, all three reported.
4. Posterior on significance: P(real|sig) = base·power / (base·power
   + (1−base)·α) — 80% → 50% → 14% for base 1/5, 1/20, 1/100.
5. Design: n = ((z_α+z_β)σ/δ)²; if the n is unobtainable, the design
   is dead — bigger effect, cheaper noise, or don't ask.

## Elaboration prompts

- Your favorite anomaly claim: compute the power of the original
  study's design against a *realistic* effect (half the reported).
  What fraction of the claimed significance survives?
- The three-way verdict, applied to something you own or trade: write
  all three lines with numbers, especially the tradable one
  (capacity, drawdown tolerance, mandate).

## Interleaved problem

An anomaly: 10bp/month, monthly SD 1.5%, 15 years, costs 8bp/month.
(a) t? (b) Economic verdict? (c) If true effect is really 6bp, what
power did the 15-year test have? (d) Design the test that would
resolve it.

<details><summary>Reference answer</summary>

(a) SR_m = 0.001/0.015 = 0.0667 → t = 0.0667·√180 ≈ 0.89 — NOT
significant. (Wait — the claim said significant? It isn't: the
anomaly as stated fails its own test. If a paper reports significance
on these numbers, something else (overlapping windows, subsample
selection) is doing the work.) (b) Gross 10bp vs costs 8bp = 2bp net
— even if real, economically dead at any scale. (c) SR_m = 0.06/1.5 =
0.04 → t-center 0.04·√180 = 0.54 → power ≈ Φ(0.54−1.96) ≈ 8%. (d)
n = ((1.96+0.84)·0.015/0.0006)² ≈ 4,900 months ≈ 400 years — the
design is dead: the honest move is cross-sectional pairing (kill the
common noise) or abandoning the question. **This problem's punchline
is that its own premise (a "significant" anomaly) was never possible
— catching that in a paper's tables is the skill.**
</details>

## Self-grade

- The power formula: produced three ways (analytic, simulated,
  table)?
- P(real|significant) machinery: can you defend its use to a skeptic
  ("where does the base rate come from?")?
