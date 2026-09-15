# Day 15 Review — The Significance Grill

## Retrieval (answers)

1. The grill order: effect size (money units, CI) → power
   (detectable = 2.8·SE) → multiplicity (family, Bonferroni/BH, the
   zoo at m = 300) → design honesty (overlap, pairing, clustering).
   Never the reverse — the t is the last thing you trust.
2. SE back-out: SE = effect/t. Band/effect = 1.96/t: t = 2.4 → 0.82,
   t = 3.2 → 0.61. Even strong claims carry 40–80% bands.
3. Detectable effect 2.8·SE is the 80%-power line: reported effect
   below it → the study is a non-detect for its own headline.
4. The zoo row (m = 300) is the HLZ arithmetic: the same t, two
   family sizes, two verdicts — thresholds are ex ante objects.
5. The √H overlap factor (04.13) applied to the t before any other
   verdict: uncorrected momentum 3.2 → 1.43 → null at the 1993
   family.

## The three verdicts (the mini-report, compressed)

- **Momentum:** survives *conditionally* — on overlap correction and
  on the ex ante family; the mechanism + monotonicity + replication
  are what keep it above the lottery.
- **Monday:** family-failed and cost-dead — the reference case for
  "the grill kills the trade, not the statistics."
- **Low beta:** a non-detect — consistent with 0 to ~390bp, not
  evidence for 200bp.

## Elaboration prompts

- Write the grill's four questions as a three-email review of a
  paper you actually read this month (or will read in module 06).
  Which question kills results most often, in your experience of
  these three exemplars?
- HLZ compresses the grill to one number (t > 3). State exactly what
  the compression assumes about effect size and power — and what
  breaks when those assumptions fail. (It assumes a canonical effect
  size and ignores power entirely: a t = 3 on a tiny n can be a
  non-detect for its own effect.)
- Design the *constructive* counterpart: the five results that would
  make you fund a claim you grilled to null. (Disjoint-sample
  replication; quantile monotonicity; mechanism with testable
  prediction; cost-survival; pre-registered protocol.)

## Interleaved problem

"Characteristic X: 400bp/yr, t = 3.1, n = 600 monthly, family of 60,
non-overlapping 1-month holding, no clustering (ETF-level)."
(a) SE and CI. (b) Detectable effect. (c) Bonferroni verdict. (d)
One-paragraph verdict in the grill's voice.

<details><summary>Reference answer</summary>

(a) SE = 400/3.1 ≈ 129bp; CI [147, 653]bp — positive, band 61% of
   the effect. (b) Detectable ≈ 361bp — the reported 400bp is just
   above the line. (c) Bonferroni threshold at m = 60: z = 3.34 —
   **fails** (3.1 < 3.34); expected false t's ≥ 3.1 among 60 noise:
   60 × 0.002 ≈ 0.12. (d) "A real-magnitude effect (400bp/yr, CI
   entirely positive, above its own power line) in a clean design
   (no overlap, no clustering) — but the family is the problem: at
   60 candidates the ex ante threshold is 3.34, and 3.1 is inside
   the 0.12-false-discovery expectation. Verdict: a candidate, not a
   discovery — the status changes with a disjoint-sample replication
   at corrected t ≥ 3.4, or with the family re-stated as pre-
   registered (one hypothesis, tested once)."
</details>

## Self-grade

- Can you run all four grill questions on any (effect, t, n, m) in
  under 10 minutes?
- Do you state verdicts as conditions, never as absolutes?
- Is your error log updated with every arithmetic slip from today?
