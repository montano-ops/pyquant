# Day 8 Review — Full EDA

## Retrieval (answers)

1. Liturgy: structure (n, NaNs, calendar) → headline (describe) → shape
   (histogram+KDE) → moments w/ SEs → QQ (tails) → rolling + ACF
   (dynamics) → verdict paragraph.
2. Order rationale: structure qualifies everything later; center before
   shape before tails before dynamics; each exhibit answers a fixed
   question.
3. Referee reads: histogram (mass, symmetry, KDE-vs-bins), QQ (WHERE it
   bends), rolling mean (regimes? crossings?), ACF|r| (dependence
   horizon = your block length).
4. EDA outputs hypotheses; confirmation needs new data (explore on A,
   test on B) — the snooping loop otherwise.
5. Verdict template: n/range → moments±SE → QQ bend location →
   dependence → "resembles X except Y" → disqualified models.

## Elaboration prompts

- Run the liturgy on an asset you *think* you know. Which exhibit
   surprised you? (If none, you weren't reading — go one level deeper:
  the rolling-mean crossings, the ACF|r| decay length.)
- Write the EDA section of a fictional paper so bad it's instructive
  (bare numbers, no SEs, decorative plots, verdict with no
  consequences) — then fix it. The contrast is the lesson.

## Interleaved problem

You're handed a return series with kurtosis 45, skew −2.8, rolling-vol
chart flat at 15%, ACF|r| ≈ 0 everywhere. Something is wrong — what,
and how would you prove it?

<details><summary>Reference answer</summary>

The combination is nearly impossible: kurtosis 45 + skew −2.8 means
monstrous outliers, but flat vol and zero vol-clustering say the
outliers arrived *uniformly at random* — real markets cluster their
extremes (Cont fact 3). Diagnosis candidates: (a) the series is a
*mixture* of two assets/stitched data (a mis-merge with a different
contract or a currency crisis pasted in); (b) rolling vol was computed
on ffilled/winsorized data while moments were computed raw — different
pipelines; (c) the ACF was computed on a *shuffled* copy. Prove it:
plot the time series itself and locate the extreme days on the
calendar — real crashes have neighbors; find the top-20 |r| days and
check their spacing (real: clustered; artifact: isolated or on
boundary dates like a stitch point). The data-quality step (step 0)
exists precisely for this.
</details>

## Self-grade

- Liturgy from memory, all seven, with questions?
- The verdict paragraph: written for SPY in under 10 minutes?
