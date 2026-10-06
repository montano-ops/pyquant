# Day 10 Review — Diagnostics

## Retrieval (answers)

1. Four panels: e–ŷ (A1 curve / A4 fan), e–time (A4 regimes / A5 /
   breaks), QQ vs normal & t(5) (A6 tails), |e| vs x (variance loading,
   curvature scout).
2. h_tt = xₜ'(XᵀX)⁻¹xₜ — unusualness of the REGRESSOR day; 3k/n rule.
3. Cook's D = (e²/(k·s²))·h/(1−h)² — β̂ movement on deletion; 4/n rule.
4. Dangerous quadrant: high leverage AND big residual — regime-breakers;
   high leverage alone = pinions, harmless when e is small.
5. The protocol: page → demands list → h/D top-5 → delete-refit-report
   shift → only then read the table.

## Elaboration prompts

- "Diagnostics don't approve regressions; they invoice them." Explain,
  with at least two invoices (White SEs, day-12 interactions).
- Why is Cook's D a product of leverage and residual rather than their
  sum — what would a sum-based measure get wrong?

## Interleaved problem

Your four-panel page shows: panel 1 clean; panel 2 shows |e| clusters in
2018Q1 and 2020Q1–Q2; panel 3 heavy tails vs normal, straight vs t(4);
panel 4 fan opening rightward. The table ships classical SEs and t = 2.9
on the key coefficient. Write the full disposition paragraph.

<details><summary>Reference answer</summary>

Panels 2+4 both invoice A4: variance varies by regime and loads on |x| →
report White HC1 (compute the SE; expect t to shrink; anticipate its new
value before computing — the discipline is predicting the repair's
direction). Panel 3's t(4) tails are tolerated at this n but mandate the
E3 influence protocol (top-D days probably sit inside the 2020 cluster —
report the shift). Panel 1 clean = A1 accepted. The shipped t = 2.9 is
suspended: replace with the White t, state both, add the influence-shift
line. If the White t < 2, the claim becomes "suggestive at conventional
levels under honest uncertainty" — and the plan to add data/regimes goes
in the log, not a hunt for a friendlier SE.
</details>

## Spaced repetition

- The two-page drill (E1+E2+E3 on one fit): +1 week, from blank.
- The quadrant grid (h × e) with examples: +3 months, redrawn.

## Self-grade

- Can you run the protocol in 10 minutes on a new regression?
- The E5 disposition pattern (keep/winsorize/interact/report-both): can
  you defend it against a pushy PM in either direction?
