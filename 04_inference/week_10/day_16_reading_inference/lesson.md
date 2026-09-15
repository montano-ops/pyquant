# Day 16 — Reading Inference in Papers

## 1. Warm-up retrieval (no notes)

1. What is a star in a paper table, in the two most common
   conventions?
2. A coefficient row: what do you need before you can call it a
   "result"?
3. The grill's four questions, in order.

## 2. The unit of consumption

You will consume thousands of tables and maybe write dozens. The
table is where papers make their *falsifiable* claims, and it is where
they hide their assumptions. Reading a table well is a mechanical
discipline: each row is a (coefficient, SE, design, sample, family)
tuple, and the row is a *result* only if all five are legible.

**The ten questions** (the checklist you now carry into modules 06–15):

1. **What is the unit of observation?** (stock-months? portfolio
   returns? which frequency?)
2. **What is the null?** (coefficient = 0? difference = 0? which
   contrast?)
3. **What is the design?** (cross-sectional? time-series? overlapping?
   paired?)
4. **What is the SE's flavor?** (iid? clustered where? HAC how many
   lags? robust to what?)
5. **What is the sample?** (period, universe, screens — and which
   screens are *post*-selection?)
6. **What is the family?** (how many rows, how many tables, how many
   papers in the same vein at publication time?)
7. **What is the effect in money units?** (bp/yr, not just t)
8. **Does the SE match the design?** (the design-honesty check from
   04.13)
9. **What is the economic story?** (mechanism, or just a coefficient?)
10. **What would kill this result?** (and does the paper test it?)

A table that answers none of these in its footnotes is a table that
hopes you won't ask.

## 3. Intuition — the star is not the result

"★" usually means |t| > 1.96 (5%) or |t| > 1.66 (10%). The star is a
*claim about a p-value under a stated design*. Three things the star
is NOT: evidence of effect size (a 3bp effect at t = 4 is a star; a
300bp effect at t = 1.8 is not — both are "results" in completely
different senses); evidence of the family (the star never counts its
siblings); evidence of the future (the star is in-sample, by
construction).

**Decode, don't believe.** The mechanical move: coefficient ÷ SE =
t; t × SE = the half-band; (estimate − band, estimate + band) = the
CI; money units × frequency = the annualized effect. Then the six
checklist questions. The decode takes two minutes per row; the
believe-or-not takes the rest of the reading.

## 4. A worked table (the exemplar)

A fictional paper's Table II, as they'd print it:

| Characteristic | Coef. (bp/mo) | (t-stat) |
|---|---|---|
| Momentum (12-1) | 55.0 | (3.06) |
| Size | −12.0 | (−1.33) |
| Book/Market | 18.0 | (2.57) |
| Volatility | −9.0 | (−2.25) |
| Turnover | −22.0 | (−2.75) |

*"Cross-sectional regressions, n = 2,400 stock-months per month × 10
years, OLS, t-statistics in parentheses, * at 5%."*

Decode, row by row:

- **Momentum:** t = 3.06, band = 1.96 × (55/3.06) ≈ ±35bp/mo →
  [20, 90]bp/mo ≈ [240, 1080]bp/yr. Effect is real *if* the design is
  honest. Design check: 12-1 momentum sampled monthly, 1-month
  holding → **no overlap** (holding = sampling frequency); t's are
  defensible *if* the SE isn't inflated by cross-sectional
  dependence (it isn't — each stock-month appears once).
- **Volatility:** t = 2.25 — starred at 5%… but this is **row 4 of 5
  in the same table**: the family is ≥ 5, Bonferroni threshold 2.97.
  The star is a lottery ticket, not a result. (This is the single
  most common error in factor tables: stars computed row-by-row on a
  family that is the whole table.)
- **Size:** t = −1.33 — the unstarred row is the honest one here: the
  table says "no detectable size effect in this specification," and
  the correct reading is exactly that, with the band [−29, 5]bp/mo
  saying how small "no effect" is allowed to be.

**The decode's verdict:** one defensible row (momentum, *if*
replicated), three stars that shouldn't be stars (the table is its
own family), one honest null. That is a *strong* paper by the
checklist — most real papers survive fewer questions.

## 5. On real data

You don't need data to read tables — you need the arithmetic. The
exercise runs the decode on the fictional table, then on a **real**
JT93-style excerpt (their Table I reports decile means and the W−L
spread with t's; the decode asks: what is the family? what is the
overlap? what does the t=3.0 on the spread really cover?).

## 6. Research connection

**Fama & French (1992):** their cross-sectional tables are the
template — size, beta, and B/M coefficients on 25 portfolio
portfolios, with the family being the whole table (5+ coefficients ×
several portfolio groupings) plus the *time-series* twins in the
next table. Reading FF92 well means seeing that the cross-sectional
and time-series tables test *different* nulls with *different*
families — a distinction most readers flatten. **JT93 Table I:**
the W−L t is a *one-sample* t on the spread (the paired design of
04.8, in disguise), on overlapping data (04.13) — two design flags
in one number.

## 7. Common mistakes

1. **Star = truth.** The star is a p under a design; the design is
   usually in the footnote; the footnote is usually skimmed. The
   star's error rate is the design's error rate.
2. **One table's SE for another's design.** Copying a t-threshold
   from a non-overlapping table onto an overlapping one (or
   clustering one way on another design) — the SE's flavor must
   match the design, question by question.
3. **The unstarred row as "nothing."** A row with t = −1.3 and a
   tight band is *evidence against* effects up to the band's edge —
   nulls with precision are results too (the module 13 placebo
   logic, in a table).

## 8. Reflection

- The checklist has 10 questions; a paper's footnote answers at best
  4. Where does the remaining 6 live — and who is responsible for
  answering them? (The reader: your decode is the missing footnote.)
- Tables reward *omission* (the starred row grabs the eye) and
  punish *completeness* (the family table is long and boring). If
  you were designing the journal's table style, what one mandatory
  column would you add? (The effective family size, or the
  corrected t — discuss which and why.)

## Self-check

1. A row: coefficient 4bp/mo, t = 3.4. Money units, annualized; the
   CI; the one sentence that tells you what it *can't* establish.
2. The same row is 1 of 40 in the paper's supplementary tables.
   What changes in your reading, and what single number do you
   compute?

---

**Answers:** (1) 48bp/yr; CI = 4 ± 1.96×(4/3.4) ≈ [1.7, 6.3]bp/mo
(≈ 20–76bp/yr) — precise and positive, *in-sample, under the stated
design, for this sample*. It cannot establish: that the effect
survives costs, that it is not one of 39 siblings, or that it
continues. (2) The family: 40 → Bonferroni threshold ≈ 3.43 — the
3.4 *just fails*; expected false t's ≥ 3.4 among 40 noise: 40 ×
0.00066 ≈ 0.026. Reading: "a precision result at the edge of its
family's noise" — replication is the only upgrade.
