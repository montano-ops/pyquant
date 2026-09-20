# Day 10 — Diagnostics

## 1. Why a quant needs this

Every assumption-repair so far (White, Newey–West) begins with *seeing the
violation*. Papers rarely show you their diagnostic plots — the honest
ones ran them; you run yours because a regression you haven't diagnosed is
an argument you haven't heard out. Today assembles the standard page and
adds the tool that matters most in fat-tailed data: **influence** — how
much of your β̂ is one day in October 2008.

## 2. The four-panel page, panel by panel

1. **e vs ŷ (fitted).** Any curve → nonlinearity (A1); any fan →
   heteroskedasticity (A4, day 5's repair). The single most
   information-dense plot in regression.
2. **e vs time.** Clusters of large |e| → vol regimes your SE flavor must
   respect; slow drifts → a nonstationarity you're ignoring (module 08's
   bill); level shifts → structural breaks (day 17).
3. **QQ of standardized residuals.** Systematic S-shape vs normal = fat
   tails (A6 — expected in finance, mostly tolerated at research n); vs
   t(5) it should straighten: that comparison *is* the tail diagnosis.
4. **e vs x (for each key regressor).** Mainly a multicollinearity-era
   sanity check and outlier scout; patterns here say the linear form
   missed curvature rather than noise.

The page has a reading order: panels 1–2 police the *assumptions with SE
repairs*; panel 3 polices inference *validity* (and outlier candidates);
panel 4 polices the *functional form*. No panel ever "approves" — the
question is always *which repair, if any, does this demand*.

## 3. Leverage and influence — the fat-tail machinery

- **Leverage** $h_{tt} = x_t'(X'X)^{-1}x_t$ (diagonal of the hat matrix
  $H = X(X'X)^{-1}X'$): how *unusual the regressor value* is — an extreme
  market day has high leverage *before* you look at the stock's response.
  Rule of thumb: h > 2k/n or 3k/n merits a look.
- **Influence** = leverage × residual, operationalized by **Cook's
  distance** $D_t \propto e_t^2 h_{tt}/(1-h_{tt})^2$: how much β̂ moves if
  observation t is deleted. D > 4/n or 1 = handle with care.

In returns data the top-leverage days are the crash records — and they
are *real data*, which is why day 11 treats deletion as a last resort.
The surprising practical fact: a high-leverage day with a 'typical'
residual is harmless (it sits ON the line and actually pins it down); the
dangerous quadrant is high leverage + large residual: a crash day where
the relationship itself broke. That combination is not noise to be
cleaned — it is **regime information** pointing at day 12's interaction
terms.

## 4. The protocol (what you actually do, in order)

1. Fit → plot the four panels → list what each panel *demands* (nothing /
   White / NW / respecify). Never read a t-stat before this list exists.
2. Compute h and Cook's D, look at the top 5 of each: are they real
   events (known dates) or data errors (module 05 reflexes)?
3. Re-fit WITHOUT the top-influence points and report the β̂ shift: if
   the story changes, your story is those points — say so either way
   (this comparison, not any plot, is the honest influence test).
4. Only then read the coefficient table, with the SE flavor the panels
   demanded.

This is 10 minutes per regression once drilled — and day 14's
mini-project will time you on it.

## 5. Common mistakes

1. **Plotting but not acting.** A fan-shaped panel 1 with classical SEs
   still in the table is a diagnosis ignored — the plot's only value is
   the repair it triggers.
2. **Formal-test substitution.** White-test p-values etc. are fine, but
   they *detect*; they don't *decide*. The deciding question is economic:
   "is the failure mode big enough, near my coefficients, to change a
   conclusion?" — answered by refits and SE comparisons, not another
   p-value.
3. **Cook's D as an auto-delete list.** Influence = "understand first".
   In finance the influential points are often the MOST informative
   observations (the only days the mechanism showed its teeth). Day 11
   formalizes the compromise (winsorize, report both).

## Self-check

1. Name the four panels, the assumption each polices, and the repair each
   can demand.
2. h_tt vs D_t: define each in one phrase and name the dangerous quadrant.
3. You delete the three highest-D days and β̂ moves 0.9 → 0.7. Write the
   research-log sentence. Then write it for the case where the deletion
   was motivated only by wanting t > 2.

---

**Answers:** (1) e–ŷ: A1/A4 → respecify or White; e–time: A4/A5/breaks →
White/NW/day-17 stability work; QQ: A6 → tolerate/fat-tail-aware inference;
e–x: A1 curvature → transform/interact (day 12). (2) h_tt = how unusual the
regressor day is; D_t = how much β̂ moves without it; danger = high h AND
big e together. (3) Honest version: "top-3 influence days (all Oct-2008)
shift β̂ 0.9→0.7; the relationship is regime-dependent — reported both,
adopted day-12 crisis interaction." Dishonest version: "points removed
until t > 2" — that's outcome-selection (module 13's name for it:
p-hacking by deletion), and the log entry is the confession that saves
you: results WITH and WITHOUT, decision made *before* seeing which is
prettier.
