# Day 14 Review — Mini-Project: The Predictive Regression

## Retrieval (answers)

1. Shift discipline: every predictor's last data point strictly precedes
   every response's first; aggregate within month first, then shift; the
   audit prints actual timestamps.
2. Predictive regressions differ from contemporaneous ones: persistent
   regressors (Stambaugh-flavored small-sample bias + optimistic t's),
   tiny honest R², and a much larger look-ahead surface.
3. R² ≈ 0.01 monthly can host ~50 bp/IQR of conditional spread — report
   the bp/IQR sentence alongside, never R² alone.
4. Per-name t's ±1–2 + cross-name synthesis: panel power comes from
   N names × consistency, not from any name's t. Cross-sectional SE of
   mean slope = std(slopes)/√N.
5. Stability evidence: split-half sign agreement (vs 50% noise line),
   rolling-slope plots read as estimation noise unless the cross-name
   average moves.

## Elaboration prompts

- Why is "R² = 0.9%" the beginning of a predictive claim and never the
  end? (R² is a property of (signal, horizon, noise variance); economics
  is bp × size × persistence × costs.)
- Your volume regressor 'worked' with t = 2.2 but the synthetic reveal
  said the planted volume effect was zero. What are the three possible
  worlds, and which do your own numbers support?

## Interleaved problem

Your report shows vol slope −50bp/σ (cross-name t = −3.1) on 50 names,
2010–2025. A PM proposes: "short the top-vol-decile names every month,
read me the capacity." Before module 10 even starts: list what this
regression does NOT establish for that strategy — five load-bearing
gaps.

<details><summary>Reference answer</summary>

(i) **Cross-section ≠ ranking**: a within-name time-series slope doesn't
price a cross-sectional SHORT portfolio (day 15–16: the decile spread,
not the slope, is the trade). (ii) **Costs & short side**: borrow fees,
locate availability, and the vol-decile's liquidity (module 12) — the
signal's bp/IQR is gross. (iii) **Persistence**: split-sample agreement
was 65% — out-of-sample decay is the base rate (module 13); one
regression window's −50bp is a prior mean, not a point forecast. (iv)
**Factor exposure**: the short basket is short beta and short momentum
by construction — the alpha sentence needs module 07's regressions
before it's an alpha. (v) **Capacity**: dollar volume of the vol-decile
names × participation caps (module 05) — the slope says nothing about
how much fits. "The regression supports a hypothesized direction worth
out-of-sample portfolio-level testing; it does not support a trade,
a size, or a capacity claim yet."
</details>

## Spaced repetition

- The shift-audit habit (print the timestamps): permanent, every study.
- bp/IQR conversion arithmetic: +1 month, from a table of slopes.
- The five-gap list for any predictive finding: +3 months, against a
  fresh claim.

## Self-grade

- Did your report convert EVERY slope to bp/IQR before celebrating?
- The audit's five channels: all present, with directions?
- Synthetic recovery honesty: pass, or error-log entry?
