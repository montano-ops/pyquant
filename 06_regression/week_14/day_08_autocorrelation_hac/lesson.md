# Day 8 — Autocorrelation & Newey–West

## 1. Why a quant needs this

Some of the most-quoted t-stats in finance are computed on **overlapping
observations**: momentum papers hold portfolios for months while measuring
monthly; predictive regressions project q-period-ahead returns at daily or
monthly frequency (dividend yield → next-year return); performance studies
roll 3-year windows. Each construction *re-uses the same data* q times —
and yesterday told you what assumption A5 buys. Break it, and the classical
t-stat inflates roughly like √q. Newey & West (1987) is the repair, cited
in essentially every such paper. Today you build it by hand.

## 2. The construction, felt mechanically

Take daily log prices and form the *monthly* return at **daily** frequency:
$y_t = \log P_{t+21} - \log P_t = \sum_{j=1}^{21} r_{t+j}$ — a forward
21-day sum. Even if daily returns are perfectly iid (zero true
predictability!), the series $y_t$ is autocorrelated to lag 20 *by
arithmetic*: $y_t$ and $y_{t-1}$ share 20 of their 21 daily moves.

Regressing y on any slowly-moving x (today's price level, a signal, last
month's return) leaves those shared moves in the residuals → AR/MA
structure in ε → classical SEs count each shared move as fresh
information, ~q times. **The data overlaps; your test thinks it's fresh.**

The ACF signature is unmistakable and *diagnostic*: for a q-period
overlap, the autocorrelation at lag l ≈ (q − l)/q — a straight-line decay
to zero at lag q. See that ramp in a residual ACF and you know both the
violation and, handily, the repair's lag parameter.

## 3. Newey–West: the sandwich grows a memory

White's meat was diagonal. Autocorrelation *is* the off-diagonal, so add
it back — weighted and truncated:

$$B_{\text{NW}} = \underbrace{\textstyle\sum_t e_t^2\,x_tx_t'}_{\text{White}}
+ \sum_{l=1}^{L} w_l \sum_{t} e_t e_{t-l}\,\big(x_t x_{t-l}' + x_{t-l} x_t'\big),
\qquad w_l = 1 - \frac{l}{L+1}$$

Read the two design choices: the **Bartlett weights** $w_l$ discount
distant lags (recent autocovariances estimated better than old ones); the
**truncation at L** says beyond the horizon the autocorrelation is treated
as zero — so **L must cover the mechanism**: q-period overlap → L ≥ q (the
classic sin is L = 5 against a 21-day overlap). Same bread, bigger meat:
$\widehat{\mathrm{Var}} = (X'X)^{-1} B_{\text{NW}} (X'X)^{-1}$. It's HAC —
*heteroskedasticity AND autocorrelation consistent*: White is the L = 0
special case.

## 4. The honest cost accounting

- NW SEs are usually **much larger** than classical on overlapped data —
  larger by roughly √q when the overlap is the whole story. This is not
  the estimator being conservative; it is the classical one having spent
  the same information q times.
- NW is consistent, not exact: at near-unit-root autocorrelation — which
  heavy overlap manufactures — it under-covers at research n (~10–14%
  rejection at nominal 5% in the day-18 tournament, even correctly
  lagged). The sandwich does most of the work; the *exact* repair for
  overlap remains the non-overlapped re-estimate.
- **NW does not fix a wrong model.** Overlapping *and* misspecified is
  still misspecified. And NW never touches β̂ (same as White).

## 5. Where you'll meet it (the research map)

- JT93 momentum (module 07.17): overlapping 3-month holding periods —
  the famous t-stats need HAC intuition to be read correctly.
- Long-horizon return predictability (the dividend-yield literature,
  module 09): the entire "does the forecast power grow with horizon?"
  debate is a Newey–West fight.
- Rolling performance evaluation (module 12): trailing-3y Sharpe on
  monthly data, same construction, same repair.

## 6. Common mistakes

1. **L too small for the mechanism.** L = 0–5 on 21-day overlapped data:
   you kept ~80% of the inflation. Rule: L ≥ overlap; for non-overlapped
   persistent data, the automatic floor $\lfloor 4(n/100)^{2/9}\rfloor$.
2. **Reading overlapped R².** R² mechanically *rises* with q even at zero
   true predictability (smoothing): an R² = 0.30 at horizon 12 tells you
   nearly nothing alone.
3. **NW as argument-ender.** If NW shreds your t-stat, the honest next
   step is a non-overlapped re-estimate (monthly observations, not daily
   overlap) — accept the smaller n; it's the same information counted
   once, the number NW was trying to recover.

## Self-check

1. Daily returns iid; you form forward 21-day sums at daily frequency.
   Write the autocorrelation of the y series at lag 5 and lag 21.
2. White vs Newey–West meat: state the exact extra term, the weight
   function, and how to choose L for (a) 63-day overlap, (b) monthly data
   with no overlap.
3. A paper regresses next-YEAR returns on today's yield, monthly data,
   t = 4.1 (classical). What's your first arithmetic guess at the honest
   t, and what's the cleaner re-specification?

---

**Answers:** (1) lag 5: (21−5)/21 ≈ 0.76; lag 21: 0 — the shared-days
fraction, linearly decaying. (2) Extra term: Σ_{l=1..L} w_l Σ_t
e_t e_{t−l}(x_t x_{t−l}′ + x_{t−l} x_t′) with Bartlett w_l = 1 − l/(L+1);
(a) L ≥ 63, (b) the floor formula ≈ 4 for n ≈ 500–600, or a couple of
lags past visible residual ACF. (3) q ≈ 12: classical t inflated ~√12 ≈
3.5×, so honest t ≈ 1–1.5 post-repair; the re-spec: annual observations,
non-overlapped — n/12 the size, information counted once, and data
snooping discipline (module 13) demands you report that version too.
