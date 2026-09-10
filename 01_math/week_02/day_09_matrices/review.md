# Review — Matrices

## Retrieval

1. Dimensions of the data matrix X for 2500 days × 40 assets? Its row vs its column?
2. Write Σ_ij's formula; what's on the diagonal? Why symmetric?
3. What does `rets.cov()` assume about your data (two things)?

<details><summary>Answers</summary>

1. 2500×40. Row t = cross-section (one date, all assets); column i = time series.
2. $\Sigma_{ij}=\frac{1}{T-1}\sum_t(r_{i,t}-\bar r_i)(r_{j,t}-\bar r_j)$;
   diagonal = variances; symmetric because Cov(X,Y)=Cov(Y,X).
3. Returns (not prices) as columns; a common sample period (pairwise
   complete rows by default in pandas — check your NaN structure!).

</details>

## Elaboration

- "Cross-section vs time series organizes quantitative finance." Give one
  research question of each type and name the module that handles it.

## Spaced repetition

- Σ returns tomorrow (portfolio variance), module 09 (its estimation
  failure), module 14 (PCA). Self-quiz the formula at +1 week.
