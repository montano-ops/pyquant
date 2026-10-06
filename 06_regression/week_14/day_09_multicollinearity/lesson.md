# Day 9 — Multicollinearity

## 1. Why a quant needs this

Factor research is a game of *attribution*: how much of a return belongs
to the market, how much to size, how much to value — when all three move
together. Regress a stock on SPY and QQQ (corr ≈ 0.9), or a strategy's
returns on two correlated "factors", and something unnerving happens:
both coefficients go individually insignificant, their SEs balloon, signs
can flip against economic sense — while the *joint* fit is completely
fine and predictions are untouched. If you can't read that signature, you
will misread every factor table in module 07, where collinear factors are
the entire subject.

## 2. The geometry in one breath

OLS picks the coefficients that best *separate* each regressor's
contribution. When x₁ and x₂ are nearly the same direction, the data
can't see what happens when x₁ moves but x₂ doesn't — because in your
sample, **that never happened**. The invariant lesson of
Var̂(β̂) = σ̂²(X'X)⁻¹: as the columns of X align, (X'X)⁻¹ eigenvalues
explode. Not a bug — an honest report that *the question "which of the
two did it?" has almost no answer in this data*.

The two-regressor closed form makes the arithmetic quotable:
$$SE(\hat\beta_1) = \frac{\hat\sigma_e}{\hat\sigma_{x_1}\sqrt{n}\cdot\sqrt{1-\hat\rho_{12}^2}}$$
The **variance inflation factor** is that last term squared:
$$\mathrm{VIF}_j = \frac{1}{1 - R_j^2}$$
where $R_j^2$ is from regressing xⱼ on the *other* regressors. ρ = 0.9 →
VIF ≈ 5.3 (SE ×2.3); ρ = 0.98 → VIF = 25 (SE ×5). Rules of thumb (VIF >
10 = worry) exist; the formula matters more.

## 3. What breaks and what doesn't

- **Individual coefficients: broken as separate objects.** Huge SEs,
  unstable signs, twitchy to one observation; β̂₁ + β̂₂ is often precise
  while each alone is mush (their CI is a long thin ellipse, not a box).
- **Joint significance: fine.** The F-test of "these two together matter"
  is unaffected — individual t's small + joint F large IS the
  multicollinearity signature. Learn to read it as one sentence:
  *"the pair matters; the split is unknowable at this precision."*
- **Prediction (ŷ): fine.** Extrapolating ŷ into regions where the
  regressors' correlation differs is what's dangerous — e.g., hedging
  with a fit from 2019 in March-nine-of-2020, when SPY/QQQ decoupled.
- **R²: unbothered.** Another reason R² can't arbitrate (day 3).

## 4. The remedies, in order of honesty

1. **Accept and report** — joint test + a statement that separate
   attribution is data-limited. The most under-used remedy.
2. **Restructure the question**: drop one regressor (SPY vs QQQ: if the
   research question is market exposure, one market proxy suffices),
   or combine (average the two; use their sum/difference).
3. **Orthogonalize**: regress x₂ on x₁, keep the residual as "x₂ net of
   x₁" — clean interpretation, standard in factor work (module 07's
   "HML net of the market"); the ordering choice is *theory*, not data.
4. **More data / different regimes** — the only cure that adds
   information; regimes where ρ differs are worth gold.
5. ~Ridge/penalization~ — biases toward stability; useful for prediction,
   a *non-answer* for attribution (module 14 will let you judge).

What you may not do: keep the variable whose t survived and declare the
other irrelevant — the SEs made survival a coin toss; that's
specification-by-lottery.

## 5. In the wild: factors and FF92

Module 07 lives here: SMB and HML correlate with the market and with each
other; FF's construction (2×3 independent sorts, value-weighted) is
*design* aimed at keeping factor correlations moderate — design you will
assess yourself when you rebuild the factors. And FF92's headline move —
"size and book-to-market *absorb* the explanatory power of beta" — is a
multicollinearity sentence wearing a referee's clothes: when correlated
characteristics enter one regression, the weaker-surviving coefficient's
death by SE is exactly what you studied today. Day 16 reads that table
with these eyes.

## 6. Common mistakes

1. **Dropping the "insignificant" one and keeping the story.** The joint
   F said the pair belongs; the t's said you can't know whose it is.
2. **Correlation-of-y thinking.** Checking corr(x₁, x₂) pairwise misses
   the general case: VIF_j uses R²_j against **all** other regressors —
   xⱼ can be a combination of three others with no pair above 0.5.
3. **Treating multicollinearity as an estimation failure.** Nothing is
   misspecified; β̂ is still BLUE if A2 holds. The data simply refuses to
   answer "who does it" — and data refusal is information about your
   design, not your code.

## Self-check

1. ρ(x₁, x₂) = 0.95, everything else unchanged: what happens to SE(β̂₁),
   to the joint F, and to ŷ on in-distribution points?
2. Write VIF without the letters R² being defined elsewhere. What
   regression defines R²_j?
3. Your factor regression shows β̂_size = 0.31 (SE 0.30) and β̂_value =
   0.12 (SE 0.28), joint F p < 0.001. Write the one-sentence finding a
   referee accepts.

---

**Answers:** (1) SE(β̂₁) inflates by 1/√(1−0.95²) ≈ ×3.2; the joint F is
essentially unchanged; ŷ stays precise *in the correlation regime you fit* —
extrapolation across a correlation break is where it detonates. (2)
VIF_j = 1/(1−R²_j), where R²_j is the R² of the regression of xⱼ on all
OTHER regressors — "how much of xⱼ is already explained by the rest of the
model." (3) "Size and value jointly price this cross-section (F p < .001);
the data cannot separate their individual premia at this precision (the
characteristics correlate strongly in these months; separate attribution
needs regimes where they decouple — day 15's FM slopes and day 16's FF92
table are read exactly this way)."
