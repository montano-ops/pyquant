# Day 8 — Vectors

## Warm-up retrieval (no notes)

1. What does least squares minimize? Why squared errors (two reasons)?
2. Why must you check `res.success` and multiple starting points?
3. State the volatility-drag formula and when it's large.

## 1. Why a quant needs this

"I hold 30% SPY, 20% TLT, 50% GLD. What did I make today?" is, mathematically,
one operation: the **dot product** of a weight vector and a return vector.
Almost everything in portfolio research is dot products wearing costumes.
Today makes the costume visible.

## 2. Vectors as "one number per thing"

A vector is an ordered list where *position has meaning*:

$$\mathbf{w} = \begin{pmatrix} 0.3 \\ 0.2 \\ 0.5 \end{pmatrix}, \qquad
\mathbf{r} = \begin{pmatrix} 0.010 \\ -0.002 \\ 0.003 \end{pmatrix}$$

$w_1 = 0.3$ is "the weight on asset 1" — the index *is* the asset. In code:
a numpy array, or a pandas Series where the index makes it self-describing.

## 3. The dot product: one multiplication that runs finance

$$\mathbf{w} \cdot \mathbf{r} = \sum_{i=1}^{N} w_i r_i = 0.3(0.010) + 0.2(-0.002) + 0.5(0.003) = 0.0041$$

That 0.0041 is **today's portfolio return** (simple returns, weights summing
to 1). Read the formula as: "pair up, multiply, add." In code:

```python
import numpy as np
w = np.array([0.3, 0.2, 0.5])
r = np.array([0.010, -0.002, 0.003])
port_ret = w @ r        # or np.dot(w, r) — ' @ ' is THE operator of this course
```

**Weights as portfolio identity.** $\sum_i w_i = 1$ = fully invested;
$w_i < 0$ = short; $\sum w_i = 0$ = *dollar-neutral* (module 11 builds these).
Long-short momentum from module 00's paper: $w = +0.1$ on each of the top
decile, $-0.1$ on each of the bottom — just a vector.

## 4. Norms: the size of a P&L stream

$$\|\mathbf{x}\| = \sqrt{\sum_i x_i^2}$$

The norm measures magnitude. Two uses you'll meet constantly:

- **Vectorization speed**: looping over 500 assets × 5000 days in Python is
  slow; `returns @ weights` over the whole history at once is one dot product
  per day, done in C. Research scale *requires* this habit.
- **Distance and similarity**: two return series are "close" if their
  difference vector has small norm; the **cosine of the angle** between two
  centered return vectors is (almost exactly) their **correlation** — module
  02 formalizes it, but today's exercise computes it, because the geometry
  makes the statistics obvious.

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT", "GLD"], start="2015-01-01")
rets = px.pct_change().dropna()          # T×3 matrix (tomorrow's topic)

w = np.array([0.5, 0.3, 0.2])
port_daily = rets @ w                    # every day's portfolio return, one line
port_growth = (1 + port_daily).cumprod()
```

Note what `rets @ w` did: T dot products in one expression. That single line
*is* a backtest engine's core (module 12 wraps costs around it).

## 6. Research connection

Jegadeesh & Titman's winner-minus-loser portfolio return in month $t$ is

$$R_{W-L,t} = \sum_{i} w_i^{(W)} r_{i,t} + \sum_i w_i^{(L)} r_{i,t}$$

— two dot products. Fama–French's SMB is the dot product of +1/6 weights on
three small portfolios and −1/6 on three big ones. When you read "the
long-short portfolio return is the value-weighted average of…", you now read
"it is a dot product," and you can implement it in one line.

## 7. Common mistakes

- Dotting weights with **log** returns (weights combine simple returns; logs
  don't distribute over sums — orientation day 4).
- Weights that don't sum to what you claim (1 for fully invested; 0 for
  market-neutral) — always assert it in code: `assert abs(w.sum() - 1) < 1e-8`.
- Looping when you could `@` — at research scale this is the difference
  between a second and an afternoon.

## 8. Reflection

1. Why does a dollar-neutral portfolio ($\sum w_i = 0$) still have risk?
  (Hint: it's not the *sum of weights* that measures risk.)
2. If two assets have correlation 1, what is the angle between their
  centered return vectors? Correlation −1? 0?

**Self-check:** compute $[0.2, 0.3, 0.5] \cdot [0.01, -0.01, 0.02]$ by hand,
and say what the number means.
