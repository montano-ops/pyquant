# Review — Joint Distributions & 2-Asset Portfolios

## Retrieval

1. Var(aX + bY) — full form. What does independence simplify it to, and
   what law does that prove?
2. The two-asset portfolio formulas.
3. Why does ρ<1 put some weight on the higher-vol asset at min-variance?

<details><summary>Answers</summary>

1. a²VarX + b²VarY + 2abCov; independence drops the covariance term →
   variances add → SDs add as √(sum): the √n law and √252 annualization.
2. μp = wμ₁+(1−w)μ₂; σp² = w²σ₁²+(1−w)²σ₂²+2w(1−w)ρσ₁σ₂.
3. The negative cross-term (2w(1−w)ρσ₁σ₂ reduced by ρ<1) pays for holding
   some of the riskier asset — covariance cancellation beats single-asset
   minimization.

</details>

## Elaboration

- Long-short momentum's variance contains a W−L covariance term. Describe
  the 2009 scenario where that term turns lethal (Daniel-Moskowitz
  preview).

## Spaced repetition

- This formula recurs in module 11 (construction) — instant recall
  required at +1 month.
