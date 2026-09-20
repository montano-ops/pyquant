# Day 12 — Specification: Logs, Dummies, Interactions

## 1. Why a quant needs this

The linear model you own is linear **in parameters**, not in variables —
$X$ may contain anything you can compute: log levels, squares, dummies,
products. This is not trivia: the questions asset pricing actually asks
are specification questions. *Does beta rise in crashes?* (interaction).
*Is the size premium per-doubling-of-cap?* (logs). *Does the effect
survive excluding earnings weeks?* (dummies). Today is the grammar of
those questions; days 16 and 19 will read them in FF92's syntax.

## 2. Dummies: letting the line move

A dummy $D \in \{0,1\}$ splits the sample *inside* one regression.

$y = \alpha + \gamma D + \beta x + \varepsilon$: γ is a **level shift** —
two parallel lines, one per regime. Read γ as "average difference,
holding x at any value" — the cleanest controlled comparison you own
(crash vs calm average return, same market exposure).

$y = \alpha + \beta x + \delta\,(D\cdot x) + \varepsilon$: δ is a **slope
shift** — the interaction. Now the crash-crisis question is literal:
$\beta_{\text{calm}} = \beta$, $\beta_{\text{crisis}} = \beta + \delta$,
and t(δ) tests "is the crash beta different" — day 10's regime-breakers
formalized instead of deleted.

Two discipline rules. (1) **The dummy trap**: include dummies for ALL
regimes *plus* an intercept and the columns are perfectly collinear (A3
dies) — drop one regime (the "base"), which then defines what the
intercept means. (2) **Read the main effect with the interaction
present**: in $y = \alpha + \beta x + \delta Dx$, $\beta$ is *the base
regime's* slope, not "the average slope" — papers get this wrong in
print; you won't after today.

## 3. Logs: changing the question from levels to ratios

- **log(y) on x**: β ≈ %Δy per unit of x (semi-elasticity) — growth-rate
  thinking; good when the phenomenon compounds (fund flows on
  performance).
- **y on log(x)**: β = Δy per ×e of x — diminishing effects: log market
  cap is the *canonical* transform (the size effect is per-doubling, not
  per-dollar — per-dollar would put 99% of the variation in the smallest
  decile, which is why it also rescues the regression from
  mega-cap leverage points: day 10's h scores collapse).
- **log(y) on log(x)**: β is an elasticity (β = 2: square-law impact
  models, module 12's cost work).

The transform is a *theory statement*: choosing log vs level chooses
whether you believe the world's gradient is per-dollar or per-ratio.
FF92's size variable is log(ME) — a specification choice with 40 years of
consequences (day 16).

## 4. Regime dummies done right (the crash-beta workout)

```python
D = (rolling_21d_vol > its 80th pct).astype(float)   # pre-declared rule!
fit y ~ x + D*x        # and optionally + D for the level
```

The trap to step over: **endogenous dummy mining** — trying six vol
thresholds until δ is significant. The rules are the usual ones: the
threshold rule is declared before the fit (calendar-based crisis dates,
or a pre-specified quantile), and the sensitivity is reported once. The
reward: a two-sentence finding with enormous practical content — "β rises
from 1.0 to 1.4 in high-vol regimes (t = 4)" is a direct input to hedge
sizing in exactly the states where hedges matter.

## 5. Common mistakes

1. **Interpreting main effects in interaction models as averages** —
   they're base-regime effects; average effects need the weighted
   combination (or marginal-effects arithmetic).
2. **Dummy mining** — threshold shopping for a significant δ; the
   multiple-testing bill (module 04.11, module 13) arrives with interest.
3. **Logs for comfort, not theory** — logging everything is
   specification-by-template: each log is a claim about the shape of the
   world; write the claim down ("size acts per-doubling") before fitting.

## Self-check

1. In $y = \alpha + \beta x + \delta(Dx) + \varepsilon$: write
   β_crisis, the no-difference null, and what β̂ alone estimates.
2. Why log(market cap) rather than market cap in a cross-sectional
   regression — two reasons, one economic, one statistical.
3. You fit y ~ x + D + Dx and get β̂ = 1.1, γ̂ = −0.02, δ̂ = 0.35. A
   colleague reports "average beta 1.27" by averaging β̂ and β̂+δ̂.
   When is that wrong?

---

**Answers:** (1) β_crisis = β + δ; H₀: δ = 0; β̂ alone is the *base*
(calm) slope. (2) Economic: the size effect is a per-ratio phenomenon —
per-dollar would assert a $1B→$2B step matters 1000× more than a
$100B→$101B step. Statistical: raw cap is absurdly skewed — its top
observations carry enormous leverage (h ∝ x²); the log restores leverage
parity. (3) Averaging assumes 50/50 regimes; if crises are 10% of days,
the unconditional average slope is 0.9·1.1 + 0.1·1.45 ≈ 1.135 — and if
your *exposure* to regimes differs from the sample's, even that number
lies about *your* risk.
