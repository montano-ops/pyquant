# Capstone 3 — Factor Model (Fama & French 1993)

**The paper:** Fama, E. & French, K. (1993), *Common Risk Factors in
the Returns on Stocks and Bonds*, Journal of Financial Economics 33(1).

## The question

Do size (SMB) and value (HML) factors explain the cross-section of
average returns that the market alone cannot? H₀: alphas ≈ 0 in
three-factor regressions.

## Required exhibits

1. Factor construction: 2×3 sorts (size × B/M), the six portfolios,
   SMB/HML spreads — the paper's machinery, rebuilt by hand.
2. Time-series regressions of test portfolios on [MKT, SMB, HML]:
   alphas with their t-stats (module 06's regression standard; plain
   OLS + robust-SE discussion if you precede module 06).
3. Cross-sectional check: do the loadings (betas) explain the average
   returns (the classic two-step)? Where does the three-factor model
   fail (momentum — the alpha on WML from YOUR capstone 1)?
4. Factor correlation structure and what it does to regression
   inference (multicollinearity preview).
5. A fourth factor debate: add momentum (UMD) — Carhart (1997) — and
   report what happens to the alphas.

## The bias audit

Sort-timing (June rebalancing with December book values — the
paper's convention hides a look-ahead trap; audit it), B/M data
availability (accounting data lags — module 05's problem), survivorship
in the size sort (small dead firms), and the test-asset circularity
(you test the model on portfolios built the same way as the factors).

## Deliverables

Nine notebooks + report + verdict. The deep deliverable: alpha vs beta
fluency — after this project, "it has alpha" must trigger the question
"against WHICH model, at what t, with whose standard errors?"
