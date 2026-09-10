# Day 7 — Mini-Project: The t-Statistic Laboratory

**The question:** how many years of data until a Sharpe-0.5 strategy
reaches t = 2 — and what does the road there look like? You will never
again evaluate a track record without this lab's pictures in your head.

## The experiments

### E1 — The t-road, simulated

Simulate 10,000 strategies with TRUE annualized Sharpe 0.5 (daily
μ = 0.5/√252, σ = 1%), paths of 30 years. For each year y = 1..30,
record the distribution of the running t-stat. Plot: median t(y) (the
SR√Y line), the 5th–95th percentile band, and the t=1.645 threshold.
Report: P(t ≥ 1.645) at y = 1, 5, 10, 16, 25 (the power curve,
one-sided 5%, verified against day 5's analytic Φ(SR√Y − 1.645)).

### E2 — The significance casino

Same paths, but TRUE Sharpe = 0 (the null). P(t ≥ 2 at least once
within 5 years of *rolling annual* evaluation)? — the "stop when
significant" audit: with monthly re-evaluation over y years, P(some
evaluation crosses 2) grows without bound. Measure it at y = 1, 2, 5.
(This is optional stopping — why peeking invalidates the 5%.)

### E3 — Fat tails

Repeat E1 with t(5) innovations (σ-matched). Compare P(t≥2) at y=5 and
y=25 to the normal case. Also run the E2 null with fat tails: does the
false-positive rate at each fixed horizon inflate (day 4's size
distortion)?

### E4 — Clustering

Repeat E1 with vol clustering (use `qrc.synth.synthetic_returns` with
vol_clustering=True, or your own two-regime vol). The mean is the
same; the SE isn't. Which years' power drops most, and why?

### E5 — The verdict table

One table: [model × years] → P(significant). Rows: SR=0 (false-positive
rate), SR=0.5 normal, SR=0.5 fat tails, SR=0.5 clustered. Columns:
1y, 5y, 16y, 25y. Under it, three sentences: what a significant 3-year
record proves (almost nothing), what an insignificant 3-year record
disproves (almost nothing), and the monitoring plan you'd give a
live SR-0.5 strategy.

## Method notes

- Working in *daily Sharpe units* (σ=1) makes the algebra clean:
  t = x̄·√n. Real-world σ only rescales μ.
- For E2's rolling evaluation: evaluate the t-stat on the trailing 252
  days each month from month 12 on. "Stopped at significance" = first
  crossing.
- E4: if you build your own two-regime vol, keep the *unconditional*
  σ at 1% so the comparison is fair (equal Sharpe, different noise
  path).

## The deliverable

The notebook + the table + the three sentences + a fourth: **what this
lab changes about how you read the next "our strategy showed a
significant t-statistic" claim.** This lab is module 12's MinTRL
section and module 13's deflated Sharpe, arriving early and by
construction.
