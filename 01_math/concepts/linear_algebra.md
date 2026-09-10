# Linear Algebra for Finance (one-page reference)

## Vectors

- A vector is an ordered list with meaning: $\mathbf{r} = (r_1, …, r_N)$ =
  "the return of every asset today"; $\mathbf{w}$ = "my weights".
- **Dot product** $\mathbf{w} \cdot \mathbf{r} = \sum_i w_i r_i$ = *portfolio
  return* (with simple returns).
- **Norm** $\|\mathbf{x}\| = \sqrt{\sum_i x_i^2}$ = length/magnitude.
- **Cosine similarity** of two return vectors ≈ correlation of two assets
  (after centering) — same idea, different normalization.

## Matrices

- The **data matrix** $X$: shape $T \times N$ (T dates, N assets) — exactly a
  wide pandas DataFrame.
- **Matrix–vector product** $X\mathbf{w}$: each row (a date) becomes a dot
  product with w → a T-length vector of *portfolio returns over time*.
- **Transpose** $X^\top$: swaps rows/columns; $(X^\top)_{it} = X_{ti}$.
- **Covariance matrix** $\Sigma = \frac{1}{T-1} X_c^\top X_c$ (with $X_c$
  centered columns): $N \times N$, symmetric; diagonal = variances;
  off-diagonal = covariances. `df.cov()` computes exactly this.

## The two formulas to own

1. **Portfolio variance:** $\sigma_p^2 = \mathbf{w}^\top \Sigma \mathbf{w}$ —
   a quadratic form; one line of numpy: `w @ Sigma @ w`.
2. **Normal equations (OLS):** solve $X^\top X \hat{\beta} = X^\top y$ →
   $\hat{\beta} = (X^\top X)^{-1} X^\top y$. "Regression" is *solving this
   system* — statsmodels just wraps it (module 06 unwraps it again).

## Why finance loves linearity

- Payoffs of linear instruments are linear in the underlying.
- Portfolio returns are linear in weights (with simple returns).
- Factor models assert returns are *approximately* linear in factors.
So most of quantitative research is: linear algebra + statistics on top.
