# Day 21 — Module Checkpoint: Does the Effect Survive?

## The contract

You choose **one signal**. You run the **full audit** on it: the
design stated, the honest SE computed, the power checked, the family
counted, the stability tested, the cost priced, the verdict
conditional. You run the **placebo**: the same pipeline on synthetic
data where the signal is zero by construction. You write the
**mini-report** to the rubric. That is the module 04 deliverable.

This is a checkpoint, not a lesson: the rubric is published up front,
there are no step-by-step instructions, and the solution is an
*exemplar* (one choice of signal, fully worked) — not the path you
must follow. Different signals, same audit.

## The signal menu (choose one)

**A. Momentum (3-1), cross-sectional.** On the research-50 panel
(real) / a 50-asset synthetic panel: 3-month formation, 1-month
skip, 1-month hold; top-10 vs bottom-10 monthly spread. The
JT93 skeleton at course scale. (The exemplar's choice.)

**B. The weekend effect, full audit.** The 04.12 pipeline promoted
to checkpoint standard: the H1/H2/H3 claims, the family, the
stability blocks, the cost gate, the placebo — as a report, not an
exercise.

**C. Volatility's sign.** "Last month's vol predicts this month's
return (sign or level), SPY or QQQ, 30+ years." Probably null —
the exemplar of an honest null with a tight band.

(Your own signal, defensibly specified, is also allowed — state the
hypothesis *and* the family you searched.)

## The rubric (published up front — every item must be ticked from your work)

**R1. Hypothesis.** H0 and H1 stated as a *contrast* (what minus
what, over what period). The tradable version named.
**R2. Data & universe.** Source, period, frequency, screens; the
known biases named (survivorship for any today's-list panel).
**R3. Design.** The SE's design: paired/independent, overlapping or
not, clustered or not — stated *before* the number.
**R4. Effect & CI.** Money units (bp/period and annualized), 95% CI,
band as a fraction of the effect.
**R5. Power.** Detectable effect (2.8·SE); reported effect vs the
line — stated.
**R6. Family.** How many hypotheses were in play (declared count),
Bonferroni threshold, verdict; the zoo row (m = 300) noted.
**R7. Stability.** ≥ 3 non-overlapping sub-periods; the pattern
(described, not just tabulated).
**R8. Cost.** Round-trip assumption with justification (per side,
at a stated size); net edge; net Sharpe; death cost; margin.
**R9. Placebo.** The same pipeline on synthetic data (same design,
known-zero signal); what the null world produced at this sample
size.
**R10. Verdict.** One paragraph: survives / survives conditionally /
doesn't — with the two conditions that would change it. No absolute
claims.

**Grading (self):** R1–R10 each met = checkpoint complete. Any
missing item names the day to re-read. The error log entries from
this day go into the permanent log.

## What the solution shows

The exemplar: **signal A (3-1 momentum)** on both worlds — real
research-50 data and the 50-asset synthetic null world — with every
rubric item worked, including the placebo and the cost gate. Read it
for *structure*; the numbers are its sample's, not yours.

## The last word on module 04

You now own the sentence: **every claim is (estimate, SE, family),
and every strategy is (edge, cost, turnover).** The rest of the
course — regression, factors, time series, portfolios, backtesting,
validation, ML, derivatives — is the application of those two
sentences to increasingly complicated objects. The module you're
leaving is the one that made you ask.
