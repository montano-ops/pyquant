# Module 01 — Mathematical Foundations (Weeks 1–2)

The mathematics a quantitative researcher actually needs — no more. You will
never see a proof here; you will see *notation you can read* and *formulas you
can compute*, because papers are written in exactly this language.

**The test this module prepares you for:** open Fama & French (1993) or
Jegadeesh & Titman (1993) and read the equations without flinching — not
"understand every symbol's theory", just *read*: know what is being summed,
averaged, multiplied, and regressed on what.

## Week 1 — Notation, functions, growth, optimization

| Day | Topic | You will be able to… |
|---|---|---|
| 1 | [Summation & notation](week_01/day_01_summation_notation/) | read Σ notation; write mean/variance as researchers write them |
| 2 | [Functions & linearity](week_01/day_02_functions_linearity/) | read f(x)=a+bx fluently; compute payoffs; see why finance is linear-obsessed |
| 3 | [Exponents & logarithms](week_01/day_03_exponents_logs/) | compound returns; geometric vs arithmetic means; annualize correctly |
| 4 | [Calculus I: change](week_01/day_04_calculus_change/) | read dY/dX as "sensitivity"; compute finite differences |
| 5 | [Calculus II: optimization](week_01/day_05_calculus_optimization/) | minimize squared error numerically; understand least squares before regression |
| 6 | [Review](week_01/day_06_review/) | retrieve it all, cold |
| 7 | [Mini-project: return arithmetic you can trust](week_01/day_07_mini_project_return_arithmetic/) | build & test your own return-conversion toolkit |

## Week 2 — Vectors, matrices, portfolio mathematics

| Day | Topic | You will be able to… |
|---|---|---|
| 8 | [Vectors](week_02/day_08_vectors/) | compute portfolio returns as dot products; think in vectors |
| 9 | [Matrices](week_02/day_09_matrices/) | organize data as T×N matrices; build a covariance matrix |
| 10 | [Matrix multiplication & portfolio variance](week_02/day_10_matrix_mult_portfolio_variance/) | compute wᵀΣw; derive the diversification effect |
| 11 | [Linear systems & OLS geometry](week_02/day_11_linear_systems_ols/) | solve normal equations by hand; estimate beta before statsmodels |
| 12 | [Optimization with constraints](week_02/day_12_optimization_constraints/) | compute a minimum-variance portfolio under constraints |
| 13 | [Review + decode paper equations](week_02/day_13_review_paper_equations/) | translate FF93/JT93 equations into plain English and pseudocode |
| 14 | [Mini-project: portfolio variance laboratory](week_02/day_14_mini_project_variance_lab/) | full diversification study with a written interpretation |

## Reference sheets

- [concepts/notation.md](concepts/notation.md) — the symbol glossary (used by every later module)
- [concepts/linear_algebra.md](concepts/linear_algebra.md) — vectors/matrices for finance, on one page

**Checkpoint:** the module review ([review/](review/)) is a cold-readings test:
five equations from real papers, translated and computed.
