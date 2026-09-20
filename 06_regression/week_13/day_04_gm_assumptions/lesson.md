# Day 4 — The Gauss–Markov Assumptions

## 1. Why a quant needs this

Day 3's SE formula was sold with fine print: "residuals well-behaved."
Today you read the fine print. Every published t-stat is a promise that a
list of assumptions held; a large fraction of empirical finance is the art
of noticing which one **didn't**, and charging the right repair. The list
is short enough to memorize and consequential enough to run your career.

## 2. The assumptions, what each buys

**A1 · Linearity in parameters.** $y = X\beta + \varepsilon$ is the right
functional form. *Buys:* the model is the model. *Breaks via:* nonlinear
payoffs (options, crash-sensitive betas), threshold effects, regime
switches. *Repair:* respecify (day 12), not re-test.

**A2 · Exogeneity: $E[\varepsilon \mid X] = 0$.** The regressor carries no
information about the error term. *Buys:* **unbiasedness** — the reason β̂
means anything. *Breaks via:* omitted variables correlated with $x$
(a sector factor hiding inside a "stock-picking" regression), simultaneity
(price affects volume affects price), measurement error in $x$. *Repair:*
a better model. **No SE trick fixes A2** — this is the only assumption
whose failure you cannot patch with a sandwich estimator.

**A3 · No perfect collinearity.** The regressors are not exact linear
combinations. *Buys:* existence of $(X'X)^{-1}$. *Breaks via:* duplicated
factors, the dummy trap (day 12), silent data bugs (constant column
twice). *Repair:* drop or combine (day 9, near-failure included).

**A4 · Homoskedasticity: $\mathrm{Var}(\varepsilon_t) = \sigma^2$.**
Constant error variance. *Buys:* the classical SE formula's validity —
and OLS's *efficiency* (best linear unbiased). *Breaks via:* volatility
clustering (your module 03 stylized fact #1) and cross-asset vol gaps.
β̂ stays unbiased (A2 intact!); the **default SEs lie** — in either
direction, simulation will show you which today. *Repair:* White (day 5).

**A5 · No autocorrelation: $\mathrm{Cov}(\varepsilon_t, \varepsilon_s) =
0$.** *Buys:* same as A4 for time series. *Breaks via:* overlapping
observation windows (counting the same information q times), stale prices,
persistent omitted factors. *Repair:* Newey–West (day 8).

**A6 · Normality of ε** (optional, for small samples). *Buys:* exact t/F
finite-sample distributions. *Breaks via:* fat tails (stylized fact #2).
*Repair:* nothing, usually — at $n \gtrsim 500$ the CLT does the job
(module 04); the tails cost *power*, not validity.

## 3. The hierarchy of failure

Not all breaks are equal. Order them by what the failure destroys:

1. **A2 failure → β̂ biased/inconsistent.** Fatal to the substance. No
   estimator patch; rethink the model. (This is why "the SEs were robust"
   cannot save a badly specified signal.)
2. **A4/A5 failure → default SEs wrong, β̂ still unbiased.** Fatal to the
   *inference*, routine in returns data, patchable with sandwich SEs.
3. **A6 failure → small-sample t distribution off.** Usually harmless at
   research sample sizes.
4. **A1/A3** are specification/existence issues — visible immediately.

Practical rule of the module: **worry about A2 with your brain (theory,
timing, measurement), and about A4/A5 with your SE choice** (the sandwich
menu, days 5 and 8).

## 4. Where returns data stands, assumption by assumption

| Assumption | Daily stock ~ market | Cross-section monthly | Overlapping horizons |
|---|---|---|---|
| A1 linearity | ~ok (crash nonlinearity lurks) | ~ok | ok |
| A2 exogeneity | plausible short-run | fight about it forever | ok mechanically |
| A4 homoskedastic | **broken** (vol clusters) | **broken** (vol spreads) | broken |
| A5 no autocorr | ~ok daily | ~ok monthly | **broken by design** |
| A6 normality | **broken** (t(3–5) tails) | broken | CLT helps |

One glance tells you why "OLS with default SEs" is almost never the right
final answer in this field — and why the rest of the week is SE repairs.

## 5. Common mistakes

1. **"Fat tails break OLS."** They don't — β̂ stays unbiased and consistent
   (A2–A5 can all hold with t(5) noise); tails dent small-sample inference
   and estimator efficiency. The fashionable remedy (robust regression) has
   its own costs (day 11).
2. **Checking assumptions by eyeball only.** A residual plot is a first
   alarm; A2 fails silently (you cannot see an omitted variable in
   residuals) — its check is *economic reasoning*, not a plot.
3. **Treating the sandwich as a specification cure.** White/Newey–West
   repair inference *given* the model; they do not remove omitted-variable
   bias. A robust SE around a biased β̂ is a precise wrong number — the
   worst kind.

## Self-check

1. Order A1–A6 by cost of failure and justify the top of your ranking.
2. Vol clustering violates which assumption(s), and what survives intact?
3. "My residuals are non-normal, so my β̂ is biased." Diagnose the two
   errors.

---

**Answers:** (1) A2 first (bias — no patch), then A4/A5 (inference —
patchable), then A6 (small samples), A1/A3 as specification/judgment
issues. (2) A4 — conditional variance varies; A2 can hold (yesterday's e
still mean-zero given x), so β̂ stays unbiased while default SEs misstate
precision. (3) Error one: normality is not an unbiasedness requirement —
A2 is; error two: at research n the t-test is robust to fat tails
anyway (module 04's size-distortion table: CLT repairs by n ≈ 500–1000).
