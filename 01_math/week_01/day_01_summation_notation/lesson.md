# Day 1 — Summation and Notation

## Warm-up retrieval (no notes)

1. Which return definition aggregates over time by addition?
2. What does `Adj Close` approximate?
3. What was the mechanism behind the "champion" strategy in orientation day 5?

## 1. Why a quant needs this

Open any paper. Within three lines you will meet something like:

$$\bar{R} = \frac{1}{T} \sum_{t=1}^{T} R_t$$

This is not decoration — it is the *entire computation* of "average return",
compressed. Σ notation is the language papers are written in; today you learn
to read it, write it, and translate it to code in both directions.

## 2. Reading Σ from the inside out

$$\sum_{t=1}^{T} r_t = r_1 + r_2 + \cdots + r_T$$

Read the symbol as a **for-loop**:

- **below** the Σ: the index and where it starts (`for t in range(1, T+1)`)
- **above**: where it ends
- **to the right**: the expression evaluated each pass (`r_t`)

So $\sum_{t=1}^{T} r_t$ is literally:

```python
total = 0.0
for t in range(T):
    total += r[t]
```

and $\frac{1}{T}\sum_t r_t$ is `total / T` — the mean. The bar notation
$\bar{r}$ ("r-bar") is the same thing, compressed once more.

**Double sums** appear the moment there are both assets and dates:

$$\sum_{t=1}^{T}\sum_{i=1}^{N} r_{i,t}$$

— a nested loop: for each date, for each asset, add. Subscripts carry the
data structure: $r_{i,t}$ is "asset $i$, date $t$" — an entire matrix hiding
in one symbol.

## 3. The formulas you must be able to read (and compute)

**Sample mean** — $\bar{r} = \frac{1}{T}\sum_{t=1}^{T} r_t$

**Sample variance** — $s^2 = \frac{1}{T-1}\sum_{t=1}^{T} (r_t - \bar{r})^2$

Two things to notice in the variance formula, both of which matter enormously
later: the **squared deviations** (distance from the mean, made positive —
this is "risk" as finance uses it), and the **T−1** (Bessel's correction —
using the estimated $\bar{r}$ eats one degree of freedom; module 03 shows
what happens if you ignore it).

**Compounding (the product operator)** — growth of $1 over T periods:

$$G = \prod_{t=1}^{T}(1 + r_t) = (1+r_1)(1+r_2)\cdots(1+r_T)$$

Π (capital pi) = "multiply them all", exactly as Σ = "add them all".
Log returns turn the product into a sum: $\ln G = \sum_t \ln(1+r_t)$ — the
single most useful identity in return arithmetic (day 3).

## 4. Python: the loop is the reading; the vector is the doing

```python
import numpy as np
r = np.array([0.01, -0.02, 0.03, 0.005])

mean_loop = sum(r[t] for t in range(len(r))) / len(r)   # the Σ, literally
mean_vec  = r.mean()                                     # same thing
var_loop  = sum((r[t] - mean_vec) ** 2 for t in range(len(r))) / (len(r) - 1)
var_vec   = r.var(ddof=1)                                # ddof=1 -> the T-1
```

**`ddof=1` is the T−1.** NumPy's default is `ddof=0` (population variance);
pandas' default is `ddof=1` (sample). Mixing defaults silently changes
every variance, covariance, Sharpe, and t-statistic you ever compute. Pick
`ddof=1` for research on samples, always, everywhere, forever.

## 5. On real data

```python
from qrc.data import get_prices           # or qrc.synth.synthetic_prices
px = get_prices("SPY", start="2015-01-01")
r = px["SPY"].pct_change().dropna()
print(r.mean(), r.var(ddof=1))
```

Typical output for daily SPY: mean ≈ 0.0004, variance ≈ 0.0001. Hold on to
the *scale*: the mean is tiny, the variance is tiny, but the ratio (mean per
unit of standard deviation) is what a strategy lives on.

## 6. Research connection

Jegadeesh & Titman (1993) define their formation-variable in exactly this
notation: the stock's return over months $t-12$ to $t-2$ is
$\prod_{j=2}^{12}(1+R_{i,t-j})$ — a *product*, over a *sub-range* of the
past, per stock. You could not implement their Table 1 without reading it.
Fama & French (1993)'s "average return of portfolio p" is
$\frac{1}{T}\sum_t R_{p,t}$ with a portfolio subscript added. The notation
you learned today is ~90% of the mathematical notation in those papers.

## 7. Common mistakes

- Reading $\sum_{t=1}^{T}$ as "sum everything" when the *expression* contains
  a second index ($\sum_t r_{i,t}$ sums over time for a *fixed* asset $i$).
- Forgetting that $\frac{1}{T}\sum$ is a single operation (mean), not two.
- `ddof` roulette: numpy default 0, pandas default 1. Standardize on 1.

## 8. Reflection

1. Why does the variance formula square deviations instead of just summing
   them? What would "sum of deviations" give instead?
2. Where could a silent `ddof` mismatch corrupt a research result you will
   build later (think: variance → Sharpe → t-stat)?

**Self-check:** write the sample variance formula from memory, then say in
words what each of its four components does.
