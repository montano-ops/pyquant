# Day 18 — Which SE When

## 1. Why a quant needs this

Every regression you will ever report needs ONE answer to one question:
*which standard error, and why that one?* You now own all four of the
course's flavors — classical, White/HC, Newey–West/HAC, Fama–MacBeth —
each matched to a violation pattern. Today consolidates them into the
routing table in your head by the method the module has used from the
start: a simulation tournament where the truth is planted, and estimators
either hold their nominal 5% rejection rate or confess. The output is a
table you will consult for years — and the confidence that comes from
having measured it, not read it.

## 2. The two questions that route you

Everything reduces to two diagnostic questions about the residuals
**under the model you specified**:

**Q1 — Is there cross-SECTIONAL dependence (panel structure)?** Same
period shared by many units → residuals correlate across units. If yes:
pooled SE flavors are disqualified on arrival; go Fama–MacBeth
(time-averaged cross-sections) or, from module 09, cluster by date/time.

**Q2 — Within a series, is there (a) heteroskedasticity and/or
(b) autocorrelation?**
- Neither → classical SEs are *correct* (and efficient — don't repair
  what's healthy; robust SEs cost power).
- Heteroskedastic only → White (diagonal meat).
- Autocorrelation (with heteroskedasticity for free) → Newey–West, lag ≥
  mechanism horizon.

The diagnostics that answer them, from day 10's page and day 15's
routine: residual correlation across units (Q1); var(e) by |x| and time
bucket + ACF(e) and the overlap's ramp (Q2a/b). Route FIRST, compute
SEs second: the flavor decision is driven by data structure, never by
which t comes out prettier.

## 3. The tournament (your exercise builds it)

Four planted worlds, all with true β known, nominal 5% tests:

| world | data | honest SE |
|---|---|---|
| iid | single series, GM holds | classical (White/NW slightly noisy) |
| het | variance rises with \|x\| | White |
| overlap | forward-21 sums at daily freq | Newey–West, L ≥ 21 |
| panel | 50 names × 120 months, common factor | Fama–MacBeth |

Each world × each applicable estimator → the rejection-rate matrix. The
claims your run will verify (or refute — log either): the classical
column holds size ONLY in the iid world; White repairs het and nothing
else; NW repairs overlap and nothing else; pooled-anything is useless in
the panel world while FM holds ≈ 5% everywhere it applies. Robust SEs in
the iid world cost a little calibration/efficiency but nothing tragic —
the asymmetry (under-robust: disasters; over-robust: small tax) is why
applied finance defaults to robust.

## 4. Reading stranger's tables with this in hand

The everyday application is not running regressions — it is *reading*
them. With the tournament felt, the rules:

1. **No SE flavor named → treat t as an upper bound on itself.** In
   returns data the prior probability that classical is right is small;
   your mental haircut's size is the tournament's classical column.
2. **Flavor named but wrong for the obvious violation** ("White" on
   21-day overlaps; "robust" on a 500-stock panel with no clustering) →
   same treatment, plus a note about what the right flavor would plausibly
   do (for overlap: t/√q-ish; panel: t/2–4).
3. **FM or cluster named → ask whether the slope series autocorrelates**
   (regime-persistent premia) and, for clustering, which TWO ways it was
   done (firm only? time only? two-way?) — module 09 will make you the
   person who runs those, and 13 will make you the person who demands
   the multiplicity account on top.

## 5. Common mistakes

1. **SE shopping**: choosing the flavor after seeing t's. The route must
   come from the diagnostic questions; the moment the t's pick the SE,
   the SEs stop meaning anything (day 12's mining logic, module 13's
   formal case).
2. **Robust-ness confusion**: "robust standard errors" unlabeled in a
   methods section could mean any of the four (+ bootstrap). Demand the
   qualifier; be the author who provides it.
3. **FM-forgetfulness**: FM is for cross-section-per-period panels with
   a priced-characteristic question; for a single time series it doesn't
   apply (and for two-way panel dependence, even FM is incomplete —
   module 09's two-way clustering).

## Self-check

1. State the two routing questions and the estimator each branch ends at.
2. Nominal-5% rejection rates, from your tournament, for classical SEs
   in each of the four worlds — the single row that justifies this whole
   module.
3. A paper reports pooled OLS, 40k firm-months, "t = 7.8, robust SEs."
   Your three-line assessment?

---

**Answers:** (1) Q1 panel? → FM/cluster-by-date; Q2a heteroskedastic? →
White; Q2b autocorrelated? → NW at the mechanism horizon; neither →
classical (and don't overpay for robustness). (2) ~5% in iid; ~20% het;
~60–65% overlap; ~35–40% panel — i.e. classical is a false-positive machine
outside its one world. (3) "Pooled + 'robust' on a panel almost surely
means White at best — which does nothing about cross-sectional
dependence; with typical same-month ρ̄ ≈ 0.3–0.5 the honest-t is plausibly
3–4× smaller, i.e. ~2–3; the claim and its 'robust' label both need the
FM/cluster version before reporting."
