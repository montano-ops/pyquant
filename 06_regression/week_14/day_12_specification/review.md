# Day 12 Review — Specification: Logs, Dummies, Interactions

## Retrieval (answers)

1. D-level shifts the intercept (two parallel lines); D·x shifts the
   slope (interaction) — β_crisis = β + δ; t(δ) tests the difference.
2. Dummy trap: all-regime dummies + intercept are perfectly collinear
   (A3) — drop one regime; the dropped one becomes the "base" the
   intercept describes.
3. With an interaction present, β̂ is the BASE regime's slope, never the
   average slope.
4. Log-x answers "per ratio" questions (log mcap = size effect per
   doubling); also rescues leverage from skewed regressors. Log–log =
   elasticity.
5. Threshold/threshold-like choices are pre-declared; sensitivity
   disclosed; mined thresholds are selection, not discovery.

## Elaboration prompts

- "An interaction is a question, not a feature." Give two research
  questions that are literally a D·x term (crash betas; effect-in-
  recessions) and one that is NOT (think: level difference with slopes
  assumed equal).
- Why does dropping the level dummy D while keeping D·x usually poison
  δ̂, and always require a defense?

## Interleaved problem

A paper regresses monthly stock returns on prior-month return and finds
β̂ = +0.04 (momentum-ish, t = 2.1). You add a "2008–09" dummy interaction:
β̂_calm = +0.06 (t = 2.6), δ̂ = −0.11 (t = −3.0) — the effect REVERSED in
the crisis. The authors decline to report your variant "because our
sample is mostly calm months." Two-paragraph referee response covering
the statistics and the rhetoric.

<details><summary>Reference answer</summary>

Statistics: the pooled +0.04 is an exposure-weighted average of two
regimes the data can clearly separate (δ t = −3.0); reporting it as "the
effect" commits the base-vs-average confusion in reverse — it is neither
the calm effect (+0.06) nor the crisis one (−0.05). The informative table
is the interaction fit, with both regime slopes and their SEs; the pooled
number belongs in a footnote measuring how much of the pooled estimate
the crisis minority contributed. Rhetoric: "mostly calm months" is the
argument FOR your variant, not against — the pooled slope hides a full
reversal in precisely the states where predictability matters most for
risk and execution (module 07.18's momentum crashes are exactly this
phenomenon in the wild). Suppressing regime splits on grounds of their
rarity prices regimes at their frequency rather than their impact.
</details>

## Spaced repetition

- The interaction grammar (β̂, δ̂, β̂+δ̂, t(δ)): +1 week, rebuilt on a
  fresh pair.
- Logs/log2 ratio transforms with their theory sentences: +1 month.

## Self-grade

- Can you state which coefficient needs the addition, unprompted?
- The two reasons for log(size), with the leverage story?
- The search-max vs rule-chosen two-column honesty: your own E5 — did you
  log it?
