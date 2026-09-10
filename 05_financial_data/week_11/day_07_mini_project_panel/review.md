# Day 7 Review — Research Panel v1 (debrief)

## Reference: what a strong quality report contains

1. **panel_info** (50 rows × ~10 cols): first, last, n, NaN%, n_div,
   n_split, min_price, median_DV, max zero-run, n(|r|>25%).
2. **The exception dispositions** — every flag gets one of:
   verified-real (with evidence: news date, action in the actions
   table), fixed (with the fix stated), excluded (with the reason and
   the selection effect of the exclusion).
3. **NaN lattice heatmap**: the listing map at a glance — IPO ramps,
   delist cliffs, halt stripes.
4. **Cross-checks**: split dates vs raw jumps (each 2:1 split = one
   ~−50% raw "return"); dividend dates vs adj-raw gaps (each ≈ D/P);
   volume-zero days vs stale prices.
5. **The bias paragraph with numbers**: alive-today universe →
   survivorship content bounded by the graveyard simulation (module
   03.1's demo at 5%/yr death, −4%/yr dead-gap → 0.5–1.5%/yr
   inflation); large-cap momentum conclusions survive it, small-cap
   and reversal claims do not.

## Synthetic-mode grading (the injected defects)

If your report didn't catch: 5 late-listers (leading NaN blocks), 3
early-delisters (trailing), 1 halt gap (interior stripe + phantom
return on resumption), 1 stale series (zero-runs + missing vol) —
then the checks, not the data, need work. **A quality report is a
detection instrument; the synthetic panel with known defects is its
calibration.** (This is the course's method — test estimators against
worlds you control — applied to pipelines.)

## Common failure modes (seen in real first attempts)

- panel_info printed but never READ: 47 clean rows and 3 weird ones —
  the weird ones are the report's entire purpose.
- Dispositions missing: "META has leading NaNs to 2012" is an
  observation; "IPO May 2012, verified, expected" is a disposition.
- The bias paragraph as boilerplate: "survivorship may affect
  results" says nothing — "this universe deletes ~5%/yr of
  disappearances; bounding simulation: 0.5–1.5%/yr of mean-return
  inflation; conclusions restricted to liquid large caps" is a
  paragraph.

## What this panel enables (and forbids)

Enables: large-cap momentum/reversal/vol studies, cross-sectional
factor sorts on 50 liquid names, capstone 1's decile machinery (with
50 names, use quintiles).

Forbids: population claims about "stocks" (survivors only), small-cap
effects, delisting-sensitive claims, anything whose edge lives in the
names this universe deleted. **Stating the forbidden list in the
panel's README is the professional habit — the panel is a tool with a
labeled domain of validity, like any instrument.**

## Next module pointer

Module 06 takes this panel into regression — but week 12 first
finishes the data story: delisting returns (Shumway 1997), the
points-in-time discipline, and the final panel audit that capstone 1
will inherit.
