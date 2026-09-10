# Capstone 5 — Volatility Modeling (Engle & Ng 1993 + GARCH)

**The papers:** Engle, R. & Ng, V. (1993), *Measuring and Testing the
Impact of News on Volatility*, JF 48(5); the GARCH family (Engle 1982;
Bollerslev 1986) as synthesized in module 09.

## The question

Can you forecast volatility one day ahead — and does the *asymmetry*
(negative returns raise vol more than positive ones: the news impact
curve) matter for forecast quality?

## Required exhibits

1. The benchmark league: EWMA, rolling, GARCH(1,1) — one-day-ahead
   variance forecasts, scored (MSE / QLIKE — say why QLIKE is fairer).
2. **GARCH by hand**: estimate GARCH(1,1) (arch package or your own MLE
   — the latter is a rite of passage; either way, know its likelihood);
   report ω, α, β and the persistence α+β, and what persistence ≈ 1
   means for risk.
3. The news impact curve: response of vol to +2% vs −2% shocks;
   EGARCH/GJR if you're ahead of module 09 — or your own asymmetry test.
4. Forecast evaluation done right: Mincer–Zarnowitz regressions
   (realized vs forecast), with the fat-tail caveat on r² as a target.
5. The risk use: convert forecasts into one-day-ahead VaR; backtest
   exception rates at 95/99% against the nominal — the whole point of
   the model is this number.

## The bias audit

Vol-of-vol (your scoring window has regimes within regimes), the
in-sample estimation trap (roll your estimates or hold out a block),
the QLIKE-vs-MSE choice (a model can win one and lose the other — say
which you trust and why), and the 2020 problem: does anything estimated
before 2020 survive March 2020?

## Deliverables

Nine notebooks + report + verdict (tradable here = does better vol
forecasting change position sizing enough to matter? — the
vol-managed-portfolio preview, module 10).
