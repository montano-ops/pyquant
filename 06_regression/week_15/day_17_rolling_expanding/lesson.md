# Day 17 — Rolling & Expanding Windows

## 1. Why a quant needs this

Every parameter you will ever trade is an estimate over some window, and
the window is a **decision with a P&L**, not a default. Day 7 showed
rolling betas wandering; today you learn the two canonical window schemes,
what each implicitly believes about the world, and — the discipline that
changes careers — how to tell "the relationship changed" from "the
estimate breathed." Parameter stability is also a *research question* in
its own right: premia emerge and decay; your rolling estimates are how
you'll see it (and how you'll fool yourself, if day 8's overlap lesson
got rusty).

## 2. The two schemes, and their implicit faith

- **Rolling (fixed W):** estimate on the last W observations only.
  Implicit faith: *the world drifts; old data expires.* You buy
  adaptivity and pay variance: SE(β̂_rolling) ≈ σ_e/(σ_x√W) — at W = 252,
  a stock-vs-market beta SE ≈ 0.05–0.08 *every window*.
- **Expanding:** estimate on all data from t₀ to now. Implicit faith:
  *the DGP is stable; information accumulates.* SE shrinks like 1/√t —
  at the cost of carrying 2010's structure into 2026's fit, which is a
  bias the day the structure breaks.

The honest statement of the trade: rolling trades staleness for noise
(bias↓ variance↑), expanding the reverse. There is NO optimal W outside a
specific world: you choose by *the persistence of what you estimate vs
the noise you can afford* — and you state the choice, not just use it.

## 3. The constant-world wander (the discipline)

Simulate a world with a CONSTANT β = 1.0 and plot its rolling β̂ at
W = 63, 252, 1008. What you will see and must never unsee: even at
W = 252 the estimate **wanders ±0.2 with zero true variation**, and the
W = 63 line looks like a seismograph. Rolling estimates of stable
parameters *move*. Two consequences:

1. **Never interpret a rolling estimate's wiggle as regime change without
   the band.** The band is ±2·SE(W) drawn from the same regression —
   wiggle INSIDE the band is estimation noise in costume.
2. **Adjacent windows share W−1 of W points**, so rolling estimates are
   autocorrelated by construction (day 8's arithmetic again: ACF ≈
   (W−l)/W). A "persistent shift" that lasts ~W periods may be ONE event
   sliding through the window, not a new regime.

## 4. Stability as a finding, stated correctly

The grammar of claiming time-variation, three admissible forms:

1. **Band test:** rolling β̂ exits the ±2·SE corridor *often and
   persistently* (more than the 5% a constant world produces) —
   quantified against the constant-world simulation of §3, not against
   vibes.
2. **Split test (informal Chow):** β̂₁, β̂₂ on two subsamples with SE₁,
   SE₂; z = (β̂₁ − β̂₂)/√(SE₁² + SE₂²). |z| > 2 says the subsample
   parameters differ beyond estimation noise — at the cost of choosing
   the split point (ex-ante: by calendar event, e.g. Feb-2020; chosen
   ex-post = mined, day 12's rule).
3. **Interaction model (day 12's formal version):** δ̂ on a pre-declared
   regime dummy — the *cleanest* claim because the regime is defined
   before the fit.

What these buy you: the sentence "β is time-varying" becomes testable;
what they never buy: freedom from the window's overlap artifacts and the
split-point's garden of forking paths.

## 5. Window arithmetic on the desk (calibration numbers)

Stock vs market, daily, σ_e ≈ σ_x (typical megacap): SE(β̂) ≈ 1/√W.

| W | SE(β̂) | reads as |
|---|---|---|
| 63 (quarter) | ≈ 0.13 | a rumor with a confidence interval |
| 252 (year) | ≈ 0.06 | quotable with a band |
| 1008 (4y) | ≈ 0.03 | stable, but prices 2022's world in 2026 |

Hence the industry pattern: **short windows for monitoring (with bands),
long windows for levels (with dates stated), expanding windows for
parameters believed stable** (factor vols in risk models — until the
regime break makes that faith expensive, and the log gets a new line).

## 6. Common mistakes

1. **Centered windows** (`rolling(W, center=True)`) in finance: W/2 days
   of future data in every "estimate" — look-ahead so smooth it survives
   code review. In time series research all windows trail.
2. **min_periods leakage**: letting early-window estimates appear with
   thin data and treating the whole series as equally reliable — the
   early segment's SE is enormous; show it or drop it.
3. **Window shopping**: trying W = 60…500 and reporting the W where a
   coefficient is significant — the day-12 threshold crime, window
   edition; declare W by rule (e.g. "one calendar year of dailies") and
   show the fan, or the search.

## Self-check

1. Rolling vs expanding: the implicit faith of each, and the failure that
   hits each one hardest.
2. Your rolling 252-day β̂ swings from 1.05 to 1.28 over a month. Name
   the two candidate explanations and the two-line computation that
   separates them.
3. A vendor's backtest used centered 128-day windows for its signal
   smoothing. What's the violation, and what does it do to reported
   Sharpe?

---

**Answers:** (1) Rolling: the world drifts — killed by variance (estimates
too noisy to use at short W); expanding: the world is stable — killed by
staleness, i.e. pricing a dead regime into today's risk. (2) Either true β
rose ~0.23, or estimation noise did (SE at W = 252 ≈ 0.06; a 0.23 move
≈ 3.7 SEs *if* the endpoints were independent — they share 251/252 of
their data, so effective z is FAR smaller; separate them with the split
test on NON-overlapping periods, or the day-3 accumulator: a real 0.23
jump survives into fresh windows, noise reverses). (3) Centered windows
put 64 future days into every estimate — the "signal" saw tomorrow; the
inflated Sharpe is built from look-ahead, and it evaporates entirely on
the first honestly-trailing window: ask for the trailing version, and if
the vendor hesitates, the meeting is over.
