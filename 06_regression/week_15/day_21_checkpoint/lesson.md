# Day 21 — Module Checkpoint: One Regression, Honestly Specified and Honestly Certified

## Overview

Modules end in production: today you produce the study this module
rehearsed, alone, with every discipline self-imposed. The subject is
**the 12-2 momentum premium in your 50-name universe** — chosen because
it touches every mechanism the module taught (estimated characteristic,
cross-sectional panel, regime variation, noise-vs-drift adjudication)
and because it hands module 07 a concrete baton.

**The contract (read once, then don't look at the solution until your
notebook prints clean end to end):** build the study in *Exercise A*;
write the two-page report in *Exercise B*; score yourself with the rubric
below; anywhere you fail a rubric line, fix the pipeline, not the rubric.

## The honesty rubric (10 lines — the checkpoint IS this list)

1. **Pre-declaration.** The characteristic, formation rule, and universe
   are written in the notebook BEFORE any result table is computed.
2. **Information audit.** A printed line proves every characteristic
   input precedes every response it predicts.
3. **Construction defense.** The skip month is justified in one sentence
   (a referee could quote it); formation length stated.
4. **Controls.** Null characteristics quiet *and* a planted premium
   recovered within ~2 SEs — both exercised in synthetic mode BEFORE
   real-mode numbers are read.
5. **Both readings.** Quintile sorts AND Fama–MacBeth slopes shown;
   disagreement, if any, explained (not hidden).
6. **Certified SEs.** FM by construction + λ̂_t ACF displayed (NW if
   needed); non-overlapping design acknowledged; no pooled-classical t
   anywhere in the report.
7. **Regime honesty.** If the report claims ANY regime statement
   ("stronger post-2016", "decayed"), it is priced against a rolling
   band (day 17's σ√(2/W) arithmetic) — drift vs noise adjudicated, not
   asserted.
8. **Caveat table.** Proxy/universe/survivorship/truncation/multiplicity/
   slope-ACF rows, each with *direction* and *severity-for-this-study*.
9. **Traceability.** Every number in the report traces to a printed
   cell; nothing freshly minted in prose.
10. **Verdict discipline.** The verdict line states scope, reports the
    calibration (evidence strength, controls status), not just
    significance, and names the next experiment.

Scoring: 8+ lines held = pass; 6–7 = pass with named repairs; ≤5 =
redo against days 15, 18, 19 before module 07.

## What good looks like

The exemplar solution runs the whole study in **synthetic mode with a
planted +40bp/σ momentum premium** (machinery must recover it), shows
every rubric line with its artifact, and writes the report with real
numbers from that run. Your real-mode run uses the identical code; the
differences are the honest ones: power, regimes, and caveats, not
machinery.

## Pacing

- 30 min: design block + pre-declaration cell (rubric 1–3).
- 60 min: pipeline build + both controls (4) — do NOT skip controls.
- 30 min: sorts + FM + regime arithmetic (5–7).
- 20 min: caveat table + report writing (8–10).
- 10 min: self-score + commit message that lists the rubric lines held.
