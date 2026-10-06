# Day 15 — Fama–MacBeth

## 1. Why a quant needs this

Day 14's per-name regressions dodged the panel problem by averaging
slopes afterward — you already performed half of today's estimator
without its name. The full question, asked by every asset-pricing paper
since 1973: **does characteristic X get *paid* in the cross-section?** —
for each month, regress that month's returns on that month's
characteristics across hundreds of stocks; then treat the monthly slope
estimates as a time series of *prices of risk*. The machinery is two
steps and one insight. The insight deserves top billing: **each month is
ONE observation of what the market paid for X** — and a time series of
honest monthly observations never needs to untangle the cross-sectional
correlation that breaks pooled OLS.

## 2. Why pooled OLS lies here (the missing-diagonal problem squared)

Stack all (i, t) pairs: $r_{i,t} = \lambda' z_{i,t} + u_{i,t}$. Classical
SEs assume the u's are independent across ALL pairs. But on any given
month, every stock shares the market: $u_{i,t}$ and $u_{j,t}$ correlate
0.3–0.9 through the common factor. White's diagonal meat can't see it
(off-diagonal across *firms*); Newey–West's lag structure can't see it
(correlation is contemporaneous across the *cross-section*, not across
time). One mechanism note that decides everything: the failure bites
exactly when the characteristic is **persistent per name** (size, BM,
vol levels — E[z_i z_j] ≠ 0), because only then does the score z·u carry
the common-factor correlation into the slope's variance. Simulation
bottom line (you'll reproduce it): **pooled classical SEs understate by
~2–3× on persistent-characteristic panels; the 5% test fires ~35–40%.**
Every pre-1973-style pooled cross-sectional regression in the literature
carries this discount; every "cluster by date/time" modern SE is the same
insight in sandwich clothes (module 09 formalizes).

## 3. The two steps, exactly

**Step 1 — the cross-sections.** For each month t = 1..T:
$$r_{i,t} = \gamma_{0,t} + \lambda_t'\, z_{i,t} + e_{i,t} \qquad (i = 1..N_t)$$
A separate OLS per month. Collect $\{\hat\lambda_t\}$.

**Step 2 — the time series of slopes.**
$$\hat\lambda = \frac{1}{T}\sum_t \hat\lambda_t, \qquad
\mathrm{SE}(\hat\lambda) = \frac{\mathrm{std}(\hat\lambda_t)}{\sqrt{T}}$$
(adding a Newey–West correction *on the $\hat\lambda_t$ series* if the
slopes themselves autocorrelate — check the ACF, usually small.) Report
also: mean monthly R² and the share of months with $\hat\lambda_t > 0$.

Conventions worth copying from the literature: characteristics are
**cross-sectionally standardized each month** (z-scores across names per
month — so λ is comparable across time and read as "return per 1σ of
characteristic"); and characteristics are measured with data **known
before** month t's returns (FF92's accounting variables lag 6+ months —
the point-in-time discipline module 05 taught you to audit).

## 4. A worked miniature (worth 20 minutes by hand)

T = 3 months, N = 4 names, one characteristic (size z-score):

| | m1 | m2 | m3 |
|---|---|---|---|
| λ̂_t (bp/σ) | −12 | +3 | −25 |

mean = −11.3, std = 14.1, SE = 14.1/√3 = 8.2, **t = −1.4** — three eyes
are honest where a pooled regression with 12 points would print
t = −2.9 with an SE that pretended the 12 were independent. The number
you'd *act* on changed; the data didn't. (Your exercise builds this by
hand, then at scale.)

## 5. What FM gives, takes, and previews

- Robust to **arbitrary same-month cross-correlation** of residuals —
  the market jolts every month and FM never needs to model it.
- Costs: treats every month as one draw (fine at T = 300+ months); noisy
  when N is small per month (step-1 noise averages out, but slowly);
  and betas/characteristics that are *estimates* (pre-ranked betas in
  FF92) import an errors-in-variables softening of the slopes (module 09
  bills for it; mention today, quantify later).
- Modern sibling: **two-way clustering** (by firm and by date) — the
  sandwich generalization; module 09 owns it. FM remains the
  cross-section's first language: when Harvey, Liu & Zhu (2016) say "t >
  3 for new factors," the t they mean is usually an FM t.

## 6. Common mistakes

1. **Look-ahead characteristics.** z_{i,t} built from information inside
   month t's return window — the slopes then price yesterday's
   newspaper. Shift audit first, always (day 14's habit).
2. **Reporting pooled SEs because "FM and pooled slopes match".** The
   slopes often DO match (both unbiased); it's the SE that breaks. The
   match you must check is the t, and it must be FM's.
3. **Ignoring the λ̂_t series itself.** Its sign-share, drift, and
   outliers are the diagnosis of whether a premium is steady or a
   handful of months — mean(λ̂_t) with a fat right tail is a different
   finding than a steady drip; print the share-positive row.

## Self-check

1. Write the two steps and the SE formula. What single fact about
   same-month residuals makes step 2 valid while pooled SEs fail?
2. Conventions: why z-score characteristics per month, and why must
   they lag the return window?
3. FM table: λ̂ = +18bp/σ (SE 6bp, T = 480 months, share-positive 61%,
   mean R² 0.04). Compose the two-sentence summary.

---

**Answers:** (1) Monthly cross-sectional OLS per month → λ̂_t; then mean
and std/√T across months. Validity: the month-level slopes' residual
variation is *time-series* variation (market-wide jolts are inside each
λ̂_t, not between them) — the same-month cross-correlation never enters
the arithmetic; only the slopes' own (small) autocorrelation remains,
NW-repairable. (2) Per-month z-scores make λ̂_t comparable across months
(dispersion of characteristics varies through time); lagging is the
look-ahead defense — FF92's accounting data lag into June t+1 for
exactly this. (3) "A 1σ higher characteristic earned +18bp/month on
average (t = 3.0, 480 months), positive in 61% of months — a persistent
but not monotonic premium; the monthly cross-sections explain ~4% of
return variance, typical for priced characteristics."
