# Review — Summation & Notation

## Retrieval

1. Translate to code: $\frac{1}{T}\sum_{t=1}^{T}(r_t - \bar{r})^2$
2. What is $\sum_t r_{i,t}$ (note the *i*) summing over, and what stays fixed?
3. Expand $\prod_{t=1}^{3}(1+r_t)$.
4. numpy vs pandas default for variance: which ddof, and which matches the T−1 formula?

<details><summary>Answers</summary>

1. `((r - r.mean())**2).sum() / (len(r) - 1)` — the sample variance.
2. Over time (t), for a *fixed asset* i: one asset's total return summed across the sample.
3. $(1+r_1)(1+r_2)(1+r_3)$ — growth of $1 across three periods.
4. numpy `ddof=0`, pandas `ddof=1`; pandas matches T−1. Standardize on ddof=1.

</details>

## Elaboration

- Explain Σ and Π to a programmer as "for-loops", including what the
  subscripts are. Then explain why $\frac{1}{T}\sum$ deserves its own symbol.

## Spaced repetition

- Rewrite the sample variance formula from memory at +1 week (module 02 day 5
  reuses it as the definition of risk).
