# Day 2 Review — Coefficients & Residuals

## Retrieval (answers)

1. β = sensitivity/hedge ratio: +1% market → +β% asset on average, in the
   estimation window; >1 amplifier, <1 damper. NOT a statement about any
   single day.
2. α̂ = ȳ − β̂x̄ — the de-marketed mean return; convert to %/yr before
   judging, then demand its SE.
3. Identities: Σe = 0, Σxe = 0, var(y) = var(ŷ) + var(e) — all *with an
   intercept*, all by construction.
4. Idio vol = std(e)·√T; for a large single stock ~60% of *variance* is
   idiosyncratic — single-name risk is mostly company risk.
5. De-marketed return r_dm = y − β̂x = α̂ + e; in-sample corr with the
   market exactly 0; out-of-sample an estimate that drifts.

## Elaboration prompts

- Explain "residual orthogonality" without math: OLS already took all the
  linear x-information it could — what remains has none left *by
  construction*. Then the trick question: so why might residuals still
  predict x tomorrow?
- Give one example where ignoring the units of α̂ produces a false trading
  conclusion (think: "+0.03%/day" read as negligible).

## Interleaved problem

Fit on 2015–2019: β̂ = 1.10, α̂ = +0.02%/day, corr = 0.6. In 2020 the same
name realizes r = −35% while the market realizes +18%. Decompose the 2020
outcome into "explained by the fitted model" vs idiosyncratic. Then the
harder question: the 2020 residual is enormous — name the three distinct
diagnoses you would consider before calling it "company news", and the
check for each.

<details><summary>Reference answer</summary>

Explained: α̂ + β̂·18% ≈ +5%/yr (α annualized) + 19.8% ≈ +25%; residual ≈
−60%. Diagnoses: (i) **β instability** — 2015–19 β̂ is a stale estimate
(crisis co-movement rises; check with a 60-day rolling β in 2020, day 17);
(ii) **α misread** — the +0.02%/day had an SE of comparable size, so the
"explained" term was always ±15%/yr (check the CI, day 3); (iii)
**nonlinearity / omitted factor** — the name's sensitivity is state-
dependent (interaction with a stress dummy, day 12; sector factor, module
07). Only after those three fail is "idiosyncratic news" the surviving
explanation — the residual is a *diagnosis of exclusion*, not a first
resort.
</details>

## Self-grade

- The three identities, state + use?
- α̂ units conversion reflex: %/day → %/yr in one step?
- "Orthogonality is imposed, not discovered" — can you defend the sentence?
