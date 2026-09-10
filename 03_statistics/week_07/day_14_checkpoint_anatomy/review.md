# Day 14 Review — Checkpoint Debrief

## Reference skeleton (compare your report's structure)

1. **Data audit**: n, range, source, missingness, |r|>25% scan (real
   event vs split artifact), zero-runs (stale marks), calendar sanity.
   Verdict sentence: trustworthy or not, why.
2. **EDA**: describe() table; histogram (labeled bins); QQ with the
   bend location named ("left tail departs from ~z=−2.5"); skew/kurt
   WITH SEs; rolling 63d mean+vol; ACF(r) and ACF(|r|) with bands.
3. **Interrogation**: three centers (spread = robustness finding);
   SD-vs-MAD gap (fat-tail diagnostic); tail multiple (observed
   |z|>3 rate vs 0.27%); rolling-mean band vs SE (constant-μ
   consistency); κ(daily) vs κ(weekly) (aggregational Gaussianity).
4. **Report ≤400 words**: Data → Distribution → Dependence →
   Limitations → Recommendation, with numbers attached to every
   verdict.
5. **Bias audit**: selection (why this asset), window (halves),
   survivorship (this asset's graveyard), multiplicity (how many
   implicit tests).

## Typical numbers, real assets (2005→, daily)

- **XLE**: κ ≈ 8–15, skew −0.3..−0.8; heavy vol clustering (ACF|r|₁ ≈
  0.2+); leverage effect present. Recommendation pattern: normal-VaR
  disqualified; GARCH-t territory.
- **TLT**: κ ≈ 3–8 (fatter than bonds "should" be — 2020's March);
  leverage effect weak; vol regimes strong. "Bonds diversify until
  rate-regime breaks."
- **IWM**: like SPY but fatter (κ ≈ 10–20) and more negative skew —
  small-cap panic mechanics.
- **GLD**: κ ≈ 2–6, skew ≈ 0..+; the *least* equity-like — which is
  the finding (and why it sits in portfolios).

## The grading conversation (self-audit exemplars)

- **"Every statistic carries (±, n)":** if your QQ bend location has no
  z value, or your kurtosis has no SE — that's 2 points gone. The
  reader must be able to *argue* with your numbers.
- **"Actionable verdict":** "don't use normal VaR" is a hedge;
  "normal-VaR understates the 1% tail by ~4× (|z|>3 multiple 6×) — use
  GARCH-t or empirical with 500+ days" is a verdict.
- **"Bias audit specific":** "survivorship could matter" = 0 points;
  "XLE's 2010–2020 window excludes the 2008 sector massacre; re-running
  on halves, κ halves 12→9 — verdict survives" = full points.

## What module 04 adds

You can now *describe* a distribution and its stability. Module 04
gives you the machinery to *test claims about it*: confidence
intervals, t-statistics, p-values done honestly, and the
multiple-comparison crisis of modern finance (Harvey–Liu–Zhu) — the
tools that decide whether a difference you described is a difference
you can defend. Your checkpoint report's "Limitations" section is the
syllabus for the next three weeks.

## Final module grade (self)

Re-read your day-14 report against the day-1 version of yourself. Then
log in PROGRESS.md: the module's single most valuable idea FOR YOU, and
the one concept you'd fail an exam on tomorrow. That second one is
module 04's day-1 warm-up.
