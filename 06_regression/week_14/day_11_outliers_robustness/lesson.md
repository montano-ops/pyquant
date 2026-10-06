# Day 11 — Outliers & Robustness: Winsorizing

## 1. Why a quant needs this

OLS pays for errors in *squares* — a single −20% day in a thousand
influences β̂ as much as forty ordinary days. Meanwhile the standard
empirical ritual, performed in nearly every asset-pricing paper you'll
read, is one unglamorous sentence: *"all continuous variables are
winsorized at the 1st and 99th percentiles."* Today you learn what that
sentence does, what it costs, and why doing it wrong is one of the
quietest ways to move a t-stat across 2.

## 2. The two operations, exactly

- **Trimming**: DELETE observations beyond the quantiles. (Changes n;
  changes the sample; asks "what if those days never happened?")
- **Winsorizing**: CLIP values to the quantiles: $x_t \gets \min(\max(
  x_t, q_{0.01}), q_{0.99})$. (Keeps n; keeps the observation in play;
  says "I believe the direction, not the magnitude.")

Winsorizing is the field default for a reason: trimming warps time
structure (deleted days leave holes in a returns series — lethal for
autocorrelation patterns and event windows), while clipping caps the
square in OLS's loss function without touching the calendar. **np.clip is
the whole implementation; the judgment is everything else.**

## 3. What winsorizing actually buys (and the sentence it forbids)

Two distinct targets, both legit:

1. **Estimator stability.** Squared-loss estimates in fat-tailed data
   have fat sampling distributions; clipping the tails shrinks Var(β̂)
   appreciably — your SE gets *honester and smaller* when a handful of
   data-error-prone points no longer steer the fit.
2. **Data-error containment.** A bad print (a −99% "return" from a data
   glitch) identified by module 05's checks but not provable enough to
   delete gets clipped — its magnitude is untrusted, its direction is
   data.

And the forbidden sentence: "winsorized until significant." Because the
clip is a modeling choice with degrees of freedom (1%/99% vs 2.5%, on x,
on y, on both), it belongs to the *garden of forking paths* (module 13):
choose it BEFORE the hypothesis test, state it in the method section, and
show the result's sensitivity to it once.

## 4. What it silently destroys

The tails of returns data are *not* noise — they are where the risk lives.

- Winsorize **y** (returns) in a market-model regression and you have
  modeled a world where crashes are mild: β̂ drops toward its calm-regime
  value precisely because you capped the days it was most wrong. For a
  risk model that's malpractice-in-miniature.
- Winsorize **x** (the regressor: book-to-market, a characteristic) and
  you destroy the cross-section's information differentially — the extreme
  small/distressed names were carrying the gradient you claimed to
  measure. FF-style studies winsorize characteristics, not returns, for
  exactly this asymmetry.
- Different clip rules across variables in one regression = a silently
  inconsistent model.

The day's credo: **clip measurement errors, never clip the phenomenon.**
If your effect LIVES in the tails (momentum crashes, day 07's crisis
betas), winsorizing it away deletes the finding.

## 5. Beyond clipping: the one-paragraph map of robust estimation

(a) Winsorize/trim — compute-first, keeps OLS; (b) Huber M-estimators —
down-weight large residuals smoothly; (c) quantile (median) regression —
models the median, ignores tail asymmetry of the mean; (d) subsample
splits (calm/stress separately) — often the most informative "robustness
check" in finance, because tails structure the relationship, not just
the noise. Know they exist; know that this course's default answer is
(a) + reporting both fits + a deliberately honest sentence about what
the tails contain.

## 6. Common mistakes

1. **Winsorizing y in time-series regressions** for "robustness" — you
   computed the world's most reassuring *and* least useful beta.
2. **Recursive/clipped-in-place bugs**: clip once, save; don't re-clip a
   clipped series on re-runs (idempotence check in the notebook today).
3. **Reading winsorized and raw results as a vote**: "4 of 6 specs are
   significant" with spec-mining is module 13's subject; today's rule is
   *one primary spec chosen ex ante, the rest disclosed*.

## Self-check

1. Trimming vs winsorizing: the one-line difference and the one-line
   reason time-series work prefers the second.
2. Why is winsorizing returns y usually wrong in a market-model fit, while
   winsorizing the characteristic x in an FF-style cross-section is
   standard? Name the asymmetry.
3. A regression gains significance going raw → winsorized. List the two
   legitimate mechanisms and the one illegitimate one.

---

**Answers:** (1) trim deletes rows (holes in the calendar; n changes);
winsor clips values in place (calendar intact; OLS's squared loss capped).
(2) y's tails ARE the risk phenomenon — capping them rewrites the
mechanism you estimate; characteristic x tails are mostly
measurement/liquidity artifacts (one bad print ≠ information about the
cross-section's gradient) — the clipped object differs in evidentiary
status. (3) Legit: estimator stability (true β̂ variance shrinks; t moves
toward its honest value either way); legit: data-error containment.
Illegit: spec-mining the clip rule ex post for the threshold that crosses
2 — indistinguishable from the first two in print, which is why the
protocol (ex-ante rule, sensitivity disclosed) is the only defense.
