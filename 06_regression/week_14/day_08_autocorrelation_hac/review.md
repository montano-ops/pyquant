# Day 8 Review — Autocorrelation & Newey–West

## Retrieval (answers)

1. Overlap construction: forward q-period sums at higher frequency →
   shared terms → ACF(l) ≈ (q−l)/q to lag q − 1, zero at q. Arithmetic,
   not signal.
2. A5 failure cost: β̂ unbiased, classical SEs too small by up to ~√q
   when the regressor is persistent.
3. NW meat = White + Σ_{l=1..L} w_l Σ e_t e_{t−l}(x_tx_{t−l}′ +
   x_{t−l}x_t′), Bartlett w_l = 1 − l/(L+1); bread unchanged.
4. Lag choice: L ≥ the overlap; non-overlapped: floor 4(n/100)^{2/9} or
   past the visible residual ACF. Under-lagging = partial repair = false
   comfort.
5. L = 0 is White — HAC nests HC.

## Elaboration prompts

- Explain why twenty-one overlapped month-returns are "one observation
  in 21 costumes" — and why the non-overlapped re-estimate, with n/21 the
  rows, is NOT a loss of information.
- A colleague says "just use L = 4, the software default." Construct the
  smallest example that proves this wrong. (Hint: you built it in E2.)

## Interleaved problem

You regress next-quarter earnings surprises on this quarter's sentiment
score: quarterly data should be safe — but the score is itself a 3-month
moving average, and you sample monthly. Residual ACF: [0.61, 0.30, 0.05,
−0.02, 0.01]. Diagnose, choose L, and name the equivalent re-spec.

<details><summary>Reference answer</summary>

The moving-average predictor imports an MA(2) structure into any error
that co-moves with it; sampling monthly while measuring quarterly
surprises adds the overlap channel. The ACF's linear-ish decay to ~0 by
lag 3 says the effective mechanism spans ≈ 3 periods → L ≥ 3 at minimum,
and prudence says L = 4–6 verified against the sd-of-β̂ simulation. The
equivalent clean spec: quarterly sampling with a sentiment *snapshot* at
quarter-end (no MA), or keep the MA and sample quarterly end-to-end —
information counted once either way. What the ACF rules OUT: a long
mechanism — lag-6+ spikes would have demanded re-specification of the
model itself, not just a longer L.
</details>

## Spaced repetition

- Write se_nw from blank; verify vs statsmodels on one overlapped series:
  +1 week.
- Tournament result table (L vs rejection): +1 month, redraw from memory,
  then reproduce in code.

## Self-grade

- Ramp formula + its diagnostic use: cold?
- Bartlett weights and truncation: can you defend both design choices?
- The reading discipline for unlabeled t-stats: could you run it on a
  new paper tonight?
