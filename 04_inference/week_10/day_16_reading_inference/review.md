# Day 16 Review — Reading Inference in Papers

## Retrieval (answers)

1. The ten questions: unit of observation; null; design; SE flavor;
   sample (and post-selection screens); family; money units; SE
   matches design?; economic story; what would kill it.
2. Decode mechanics: SE = coef/t; CI = coef ± 1.96·SE; band/effect =
   1.96/|t|; annualize by frequency. Two minutes per row.
3. The table is its own family: 5 rows = 5 tests → Bonferroni 2.97;
   the exemplar's 4 stars → 1 survivor.
4. The unstarred row with a tight band is a *precise null*: state
   what it excludes, in money units.
5. The star is a p under a design; the design's error rate is the
   star's error rate.

## The two flags from the exemplar

- **JT93's W−L t:** overlapping 5-day design (√5 question) + family
  = the deciles, not one test; the monotonic pattern is the evidence
  beyond one t.
- **The fictional table:** 4 stars, 1 survivor; the unstarred row is
  the most informative cell (excludes ±~30bp/mo size effects).

## Elaboration prompts

- Write the ten questions as a *one-page* template with a column for
  "what the paper states" and a column for "my decode" — and apply
  it to one real table from a paper in modules 06–07 (FF92, JT93, or
  FF93) when you read it.
- A journal editor asks you to propose one mandatory table column.
  You proposed "effective family size or corrected t." Defend it in
  three sentences against "we already publish p-values."
- Explain to a co-author why their "t = 4.2, n = 8,760" result needs
  an overlap question before the magnitude question. (The design can
  change the t by √H; the magnitude is a property of the effect;
  you must know the t's denominator before you rate the numerator.)

## Interleaved problem

A table, 6 rows, t's = [3.8, 2.9, 2.6, 2.4, 2.1, 1.4], coefficients
all ~10–30bp/mo. (a) Stars at 5%. (b) Bonferroni survivors. (c) BH
survivors. (d) The expected false stars under "only row 1 is real."
(e) One-paragraph decode of the table as a *publication event*
(what it establishes, what it manufactures).

<details><summary>Reference answer</summary>

(a) Rows 1–4 starred. (b) Threshold at m=6: z = 3.20 — only row 1
(3.8) clears. (c) BH: p's ≈ [0.00014, 0.0037, 0.0093, 0.0164,
0.0357, 0.162]; rank thresholds k·0.05/6 = 0.00833k: row 1 (0.00014
≤ 0.00833) yes; row 2 (0.0037 ≤ 0.0167) yes; row 3 (0.0093 ≤ 0.025)
yes; row 4 (0.0164 ≤ 0.0333) yes; row 5 (0.0357 ≤ 0.0417) yes; row 6
(0.160 ≤ 0.05) no → **k = 5**. (d) 1 + 5×0.05 = 1.25 expected stars.
(e) "A table that looks like four results is, under its own family,
one result (row 1) plus three lottery-eligible rows that a
Bonferroni reader would delete and a BH reader would keep as a
*mostly-false declared set*. The table establishes: row 1,
conditionally on the design being honest; it manufactures: the
appearance of a 4-factor model from a 1-factor sample. The honest
reading funds row 1's replication and files the rest as
hypotheses."
</details>

## Self-grade

- Can you decode a 5-row table in under 10 minutes, family included?
- Did you write the honest-null sentence for an unstarred row?
- Is your author-email template ready (four questions, each forcing a number)?
