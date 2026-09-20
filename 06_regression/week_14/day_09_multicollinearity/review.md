# Day 9 Review — Multicollinearity

## Retrieval (answers)

1. Mechanism: x₁ ≈ x₂ = the sample never shows one moving without the
   other → attribution unknown → (X'X)⁻¹ eigenvalues explode → SEs
   balloon. β̂ stays unbiased (A2 fine); nothing is "wrong" with the fit.
2. VIF_j = 1/(1−R²_j), R²_j from xⱼ on ALL other regressors. SE_j scales
   by √VIF. ρ = 0.9 → ×2.3; ρ = 0.98 → ×5.
3. Signature: tiny individual t's, huge joint F, stable sum, R²
   unaffected.
4. VIF > 10 rule of thumb; but pairwise corr check UNDER-detects —
   three-way combinations hide (E4).
5. Remedies by honesty: accept & report jointly; restructure (drop/
   combine); orthogonalize (order = theory); add data/regimes (only real
   information); never "keep the winner."

## Elaboration prompts

- Why is the sum β̂₁ + β̂₂ precise when the parts are not? Explain with
  the negative covariance v₁₂.
- A factor model's author says "we orthogonalized value on momentum"
  instead of the reverse. What THEORY is implicit, and how would the
  table look under the reverse order?

## Interleaved problem

FF-style regression on your own book: r_strategy ~ [MKT, SMB, HML], with
corr(SMB, HML) = 0.55, corr(MKT, SMB) = 0.3. Output: MKT t = 22; SMB
t = 1.1, HML t = 1.6; joint F p < 1e-9. The PM concludes "we have no
size or value exposure, just market." Grade the conclusion and write the
corrected two-liner for the risk deck.

<details><summary>Reference answer</summary>

The conclusion over-reads inflated SEs. corr(SMB,HML) = 0.55 lifts their
VIFs to ~1.5–2 before their own vol even enters; the t's are individually
weak, but the JOINT statement p < 1e-9 says the exposures exist as a
bundle. Corrected: "Market exposure is precise (t = 22). Size/value
loadings are individually imprecise due to factor correlation (VIF ≈ 1.5–
2); jointly the three-factor model is highly significant (F p < 1e-9) —
point estimates SMB/HML are economically meaningful in size but ±60% in
precision; treat as 'exposed, magnitude uncertain', not 'absent'." The
general rule: "absence of evidence" (big SE) ≠ "evidence of absence"
(small coefficient with small SE) — quote the CI, not just the t.
</details>

## Spaced repetition

- VIF by hand + the sum-t Wald computation: +1 month, from blank.
- E4's blind spot: +3 months, reconstruct the example and the moral.

## Self-grade

- The signature sentence (small t's, big F, stable sum) on demand?
- The remedy menu in honesty order, with the forbidden fifth option?
- v₁₂'s sign and meaning cold?
