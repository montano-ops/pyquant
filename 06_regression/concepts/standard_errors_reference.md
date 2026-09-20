# Standard Errors — The Decision Table

_One reference for module 06 (built interactively on day 18; clustering is
developed fully in module 09). The classical formula assumes a world returns
data does not live in. This sheet is the repair manual._

## The anatomy (sandwich form)

Every SE below estimates $\mathrm{Var}(\hat\beta) = (X'X)^{-1}\, B\,
(X'X)^{-1}$ and differs only in the meat $B$:

| Estimator | Meat $B$ | Use when | statsmodels |
|---|---|---|---|
| Classical (iid) | $\hat\sigma^2 X'X$ | residuals homoskedastic **and** uncorrelated (rare in finance) | default |
| White / HC | $\sum_t e_t^2\, x_t x_t'$ | heteroskedastic residuals, no autocorrelation (cross-sections; vol regimes) | `cov_type="HC1"` |
| Newey–West / HAC | White $+$ $\sum_{l=1}^{L} w_l \sum_t e_t e_{t-l}(x_t x_{t-l}' + x_{t-l}x_t')$ | autocorrelated residuals: overlapping windows, persistent errors | `cov_type="HAC"`, `cov_kwds={"maxlags": L}` |
| Clustered | within-group sums of $e_t x_t$ cross-products | residuals correlated *within groups* (same date / same firm) | `cov_type="cluster"`, `cov_kwds={"groups": ...}` (module 09) |

Newey–West weights: $w_l = 1 - l/(L+1)$ (Bartlett kernel — distant lags count
less). **Lag rule of thumb: $L$ ≥ the overlap length** (21-day overlapping
windows → $L$ ≈ 21–42); the automatic floor $L = \lfloor 4(n/100)^{2/9}
\rfloor$ covers non-overlapping daily/monthly data.

## Which violation, which cost, which repair

| Symptom | Test | β̂ biased? | Default SE | Repair |
|---|---|---|---|---|
| Vol clustering / differing vols | residual plot fan shape; White test | no | wrong (either direction) | White HC1 |
| Overlapping windows | ACF of residuals: spikes to lag ≈ overlap | no | **too small** (you counted the same info ~q times) | Newey–West, $L$ ≥ overlap |
| Cross-correlation at same date (panels) | residual correlation across firms | no | far too small | Fama–MacBeth or cluster-by-date |
| Omitted correlated factor | theory, not a test of residuals | **yes** | n/a | fix the model, not the SE |
| Fat tails only | QQ of residuals | no | roughly right in big samples | nothing needed; winsorize for stability (day 11) |

## Fama–MacBeth as an SE strategy

For panel studies (assets $i$ × months $t$): run the cross-sectional
regression **separately each month**, then treat the $T$ slope estimates
$\hat\lambda_t$ as a sample:

$$\hat\lambda = \frac{1}{T}\sum_t \hat\lambda_t,
\qquad \mathrm{SE}(\hat\lambda) = \frac{\mathrm{std}(\hat\lambda_t)}{\sqrt{T}}$$

(with a Newey–West correction on the $\hat\lambda_t$ series if the slopes
themselves are autocorrelated). Each month is one observation of the price of
risk; the market-wide correlation that breaks pooled OLS never enters the
arithmetic. This is the estimator behind FF92 (days 15–16).

## The honesty table (from day 18's simulation tournament)

Nominal 5% tests, known-zero effects, badly-behaved data:

| Data regime | Classical | White | Newey–West | FM |
|---|---|---|---|---|
| iid (n = 1200) | ~4–5% | ~4–5% | ~5% | — |
| heteroskedastic (var ∝ \|x\|) | ~23% | ~4–5% | ~4–5% | — |
| overlapping (q = 21, n = 3000) | ~60–65% | ~60–65% | ~11–14% (L = 21)* | — |
| panel (50 × 120, persistent char) | ~35–40% | ~35–40% | blind (wrong axis) | ~4% |

\* HAC is consistent, not exact: at near-random-walk autocorrelation and
this n it under-covers. The exact repair is the non-overlapped
re-estimate, which the numbers in the overlap row were built to match.
Panel footnote: with *fresh monthly* characteristics (zero
cross-sectional persistence) the score's common-factor correlation washes
out and even pooled classical nearly holds size — real characteristics
persist, which is why the pooled failure is the default.

Pattern: **the right SE holds size ≈ 5%; the wrong one manufactures
t-stats.** A publishable-looking t = 2.5 under the wrong SE is often a
t = 0.8 under the right one.
