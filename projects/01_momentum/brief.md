# Capstone 1 — Momentum (Jegadeesh & Titman 1993)

**The paper:** Jegadeesh, N. & Titman, S. (1993), *Returns to Buying
Winners and Selling Losers: Implications for Stock Market Efficiency*,
Journal of Finance 48(1). You reproduce its core: 6-month formation,
1-month holding, decile portfolios, WML spread.

## The question (pre-registered in 01_question.ipynb)

Does ranking stocks on trailing 6-month return predict the *cross-
section* of next-month returns? H₀: zero spread. Economic hypothesis:
underreaction (behavioral) / compensation for crash risk (rational) —
name yours and say what evidence would separate them.

## Required exhibits

1. Decile monotonicity: average next-month return by formation decile
   (the paper's Table I shape).
2. The WML spread: mean, t-stat (Newey–West when you know it; plain +
   caveat before module 06), and the **momentum crash audit** — 1932,
   2009-style episodes where WML delivers −50%+ (Daniel & Moskowitz
   preview: the spread is long crisis risk).
3. Overlapping-portfolio machinery: why JT's portfolios overlap 6 ways,
   and what that does to your SEs (n_eff, module 02.19).
4. Cost sensitivity: spread at 0/10/50/100bp round-trip per leg.
5. Frequency-formation grid: 1/3/6/12-month formation × 1/3/6-month
   holding — the pattern JT found (short-term reversal, medium
   momentum, long-term reversal) is the map of the field.

## The bias audit (mandatory, with numbers)

Survivorship (your universe's graveyard — simulate its direction if
your data can't see the dead), look-ahead (formation returns use
t−12→t−2 — NEVER t; verify with a shift audit), rebalancing timing
(signal computed at close, executed next open/close — state and defend),
and multiplicity (your grid scanned 12 cells; which spread would you
have shown your boss?).

## Deliverables

Nine notebooks + the report (template) + the three-way verdict:
statistical / economic / tradable. The report's conclusion quotes your
own pre-registration and grades the drift between them.
