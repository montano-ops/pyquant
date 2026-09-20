# Day 20 — Weekly Review

No new material. Today closes the module's last loop: by the end you
should be able to say, without notes, (1) why Fama–MacBeth works and
when it fails, (2) what FF92's regression columns actually said and the
three mechanisms that can fake or fade them, (3) how a window choice is
a variance–bias dial, and (4) which SE goes with which failure — and run
one more cross-method retrieval before tomorrow's checkpoint.

## The week's loop

**Day 15 (machine).** FM = monthly cross-sectional regression → relative-
price series λ̂_t → average with SE = sd/√T. Sidesteps panel dependence at
estimation time (coefficients unbiased either way); the t is the time-
series mean of a stationary series. Universal cheat code honoring the
other three flavors. Watch: λ̂_t autocorrelation, weak cross-sections
(pass-through variance blow-up and EIV — bin into deciles).

**Day 16 (paper + killers).** FF92 bottom line: conditional on size,
log-BM soaks up "beta explains nothing" — absorption is attribution
under correlation; both tables (beta-flat and β-singleton) are right in
their own worlds and nothing inside a cross-sectional fit adjudicates
them. Killers: EIV in estimated regressors (attenuate; decile-bin to
kill measurement noise ~10× — the strongest mechanical argument for
quantile portfolios); overlap (no NW at month scale, NW-day horizon at
day scale); point-in-time (a measured-on-winners characteristic is a
survivorship character mutation — the obvious-forward fill is a bug even
when it prints).

**Day 17 (dial).** Rolling/expanding closed forms; window = variance
dial (SE ∝ 1/√W: 3 mo breath, 3 yr whisper); regime interpretation
legit when drift dominates the band (|movement| >> σ √(2/W)/... the
day's formula) — band = drift vs noise; expanding's alpha = information
half-life; test breaks by simple before/after arithmetic with var(t) =
SEs² — no formulas.

**Day 18 (tournament).** The standard error is a claim about the residual
process. Classical honest only iid; White repairs the cone, blind to
memory and panel share; NW ≥ horizon for overlap (consistent-not-exact:
~11–14% under-coverage at strong overlap, month-nonoverlapped re-estimate
the exact repair); FM alone survives panels. Triage flowchart: panel? FM
+ ACF → overlap? NW ≥ horizon → fan? White → else classical.

**Day 19 (study).** The full protocol — pre-declared characteristics,
strict information audit, sorts + FM, the two controls (null silence,
positive recovery), caveat table with directions — executed end to end.
The headline can be honest nothing: that IS the megacap calibration.

## Retrieval drills (20 min, closed notes)

1. Write the FM algorithm's four steps, the SE formula, and its one
   statistical assumption.
2. Write the three killers and the repair/diagnostic for each.
3. Write the SE formula for a rolling β̂_W (closed form) and state the
   bias-variance dial as one sentence.
4. Draw the flowchart from day 18's E4 from memory.
5. Write the two synthetic controls and what each gates.
6. From memory: FF92's size/β joint-table move and why it decides the
   paper.

Then the exercises — a mixed bag where the point is choosing the tool,
not the tool itself.
