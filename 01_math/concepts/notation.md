# Notation Glossary (course-wide reference)

Papers reuse a small alphabet. Learn it once; read papers forever.

## Indices

| Symbol | Meaning | In finance |
|---|---|---|
| $t$ | time index | day/month $t$; returns $r_t$ run over $t=1..T$ |
| $i$ | asset/cross-section index | stock $i$ of $N$ |
| $T$ | number of time observations | sample length |
| $N$ | number of assets | universe size |

## Basic operators

| Notation | Read as | Meaning |
|---|---|---|
| $\sum_{t=1}^{T} x_t$ | "the sum of x-t for t from 1 to T" | $x_1 + x_2 + \cdots + x_T$ |
| $\bar{x}$ | "x-bar" | sample mean $\frac{1}{T}\sum_t x_t$ |
| $\prod_{t=1}^{T}(1+r_t)$ | "the product of…" | compounding: growth of $1 |
| $x'$ or $x^\top$ | "x transposed" | row↔column flip of a vector/matrix |
| $\mathbb{E}[X]$ | "the expectation of X" | the population mean (long-run average) |
| $\hat{\theta}$ | "theta-hat" | an *estimate* of θ from data (the hat means "estimated") |

## The core objects (as you meet them)

| Notation | Object | First met |
|---|---|---|
| $r_t$ or $r_{i,t}$ | return of asset $i$ at time $t$ | 00.4 |
| $w$ (vector), $w_i$ | portfolio weights, $\sum_i w_i = 1$ for fully invested | 01.8 |
| $\Sigma$ (capital sigma) | covariance matrix of returns | 01.9 |
| $\mu$ (mu) | vector of expected returns | 01.9 |
| $\sigma^2$, $\sigma$ (sigma) | variance, standard deviation | 02.5 |
| $\text{Cov}(X,Y)$, $\sigma_{xy}$ | covariance of X and Y | 02.8 |
| $\rho_{xy}$ (rho) | correlation = Cov/(σx·σy), lives in [−1, 1] | 02.8 |
| $\beta$ (beta) | regression slope; market sensitivity | 06 |
| $\alpha$ (alpha) | regression intercept; return not explained by factors | 06 |
| $\varepsilon_t$ (epsilon) | noise / error term / innovation | 06 |
| $R^2$ | share of variance explained by a regression | 06 |
| $H_0$, $H_1$ | null and alternative hypotheses | 04 |
| $\sim$ | "is distributed as" ($X \sim N(\mu, \sigma^2)$: normal) | 02 |

## Reading conventions that trip beginners

- **Subscripts carry the data structure**: $r_{i,t}$ = "stock $i$, month $t$"
  — a whole matrix of returns hides in one symbol.
- **A sum with no limits** ($\sum_i w_i r_i$) means "over the whole relevant
  index" — here, all assets.
- **Hats distinguish estimates from truths**: $\hat{\beta}$ (estimated from a
  sample) vs $\beta$ (the unknowable truth). A large part of statistics is
  the study of how far hats sit from truths.
- **"i.i.d."** = independent and identically distributed — the default
  assumption that financial data keeps violating.
- **"conditional"** ($\mathbb{E}[r_{t+1} \mid \mathcal{F}_t]$) = expectation
  *given information available at t* — the mathematical home of trading:
  your expected next return, conditional on everything you know now.
