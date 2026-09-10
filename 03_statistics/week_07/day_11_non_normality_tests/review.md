# Day 11 Review — Non-Normality, Quantified

## Retrieval (answers)

1. JB = n(ν̂²/6 + κ̂²/24) ~ χ²(2): combines the two moment tests,
   weighted by their SEs. Lilliefors: max |ECDF − fitted Φ| — whole-
   shape distance, fitted-parameter-corrected KS.
2. Big-sample pathology: consistent tests reject any fixed alternative
   as n → ∞ — at market n's, JB flags κ = 0.5 (irrelevant) as
   "significant." Effect size over p-value, always.
3. Small-sample mirror: at n = 60 (monthly strategies), SE(kurt) ≈ 0.63
   — real fat tails sleep through the test. The test's power tracks n,
   not importance.
4. The professional package: κ̂±SE, ν̂±SE, JB/Lilliefors p, QQ
   location, and the CONSEQUENCE sentence (what this does to VaR /
   pricing / sizing, with the tail multiple).
5. Lilliefors ≠ KS: KS assumes known (μ, σ); fitted parameters absorb
   the data's moments, shrinking D — Lilliefors uses fitted-critical
   values.

## Elaboration prompts

- "Significant but irrelevant" vs "irrelevant but significant" — same
  thing? Write the distinction in two sentences and an example of each
  from this module.
- Your risk system rejects normality at n = 8,000 but the desk head
  says "so use the t." What are the THREE follow-up questions before
  agreeing? (df estimated how? Tails or center driving it? What
  changes in the VaR number and the margin policy?)

## Interleaved problem

Monthly strategy returns, n = 48: skew −0.9, excess kurtosis 2.4.
Compute JB. Verdict at χ²(2) 95% = 5.99? What is the honest
interpretation, given SE(ν̂) and SE(κ̂)?

<details><summary>Reference answer</summary>

JB = 48·(0.81/6 + 5.76/24) = 48·(0.135 + 0.24) = 48·0.375 = 18.0 —
well past 5.99: reject normality. BUT: SE(ν̂) = √(6/48) = 0.354 → skew
is −0.9 ± 0.7 (2.5 SE, real-ish); SE(κ̂) = √(24/48) = 0.707 → kurtosis
2.4 ± 1.4 (1.7 SE — suggestive, not established). The honest read:
moderately strong evidence of negative skew, weak evidence of fat
tails; the joint test rejects mainly on the skew leg. And the
consequence question dominates both: at n = 48, a single bad month
moves these estimates materially — check the worst month's leverage on
each statistic (drop-one sensitivity: recompute with and without the
worst month; if the verdict flips, the verdict IS the worst month).
</details>

## Self-grade

- JB from memory? The κ that rejects at n=504 (≈0.53)?
- Effect-size-over-p-value: applied in your own words?
