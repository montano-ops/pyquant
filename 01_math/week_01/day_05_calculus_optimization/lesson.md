# Day 5 — Calculus II: Optimization

## Warm-up retrieval (no notes)

1. Define the derivative as a "nudge ratio" in words.
2. What is convexity, and what does $f'' > 0$ imply about a critical point?
3. Name three finance quantities that are derivatives.

## 1. Why a quant needs this

Quantitative research is a sequence of optimization problems:

- **Least squares**: choose coefficients to minimize squared error — every
  regression you will run (module 06) is this, today.
- **Minimum variance**: choose weights to minimize $\mathbf{w}^\top\Sigma\mathbf{w}$
  — portfolio construction (day 12, module 11).
- **Maximum likelihood**: choose parameters to maximize the probability of
  the data — GARCH (module 09), logistic regression (module 14).

You need the *intuition* (what is being minimized, over what choices) and the
*tool* (`scipy.optimize.minimize`), not the theory of Lagrange multipliers.

## 2. The picture (which is all the theory you need)

A function $f(\theta)$ maps parameters to a number. Optimization = walking
on the $f$-surface to the lowest valley (or highest peak).

- At a valley floor, the slope in every direction is zero: $f'(\theta^*) = 0$
  — the "first-order condition".
- If the floor curves up everywhere (convex, $f'' > 0$), the valley is the
  *unique* lowest point — you can trust it.
- **Gradient descent**: from anywhere, step downhill; repeat. Slope points
  the way. (This sentence is most of machine learning, module 14.)

$$\theta_{new} = \theta_{old} - \lambda \cdot f'(\theta_{old})$$

## 3. The objective you'll minimize for six straight modules

**Sum of squared errors (SSE).** Given data $(x_t, y_t)$ and a model
$\hat{y}_t = a + b x_t$, the errors are $e_t = y_t - \hat{y}_t$ and

$$SSE(a, b) = \sum_{t=1}^{T} e_t^2 = \sum_{t=1}^{T} (y_t - a - b x_t)^2$$

Least squares chooses $(a, b)$ to minimize SSE. **Why squares?** They're
positive (errors can't cancel), differentiable (calculus works), and they
*penalize big misses quadratically* — one 2-unit miss hurts as much as four
1-unit misses. (They also make the math linear — day 11 shows the closed
form. The price: outliers dominate — module 06 revisits.)

## 4. Python: minimize it yourself

```python
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(0)
x = np.linspace(0, 1, 100)
y = 0.02 + 1.5 * x + rng.normal(0, 0.1, 100)     # "data"

def sse(theta):
    a, b = theta
    return np.sum((y - a - b * x) ** 2)

res = minimize(sse, x0=[0.0, 1.0])                # x0 = starting guess
print(res.x)                                      # [a_hat, b_hat]
```

`minimize` needs two things: the objective and a starting point. What it
returns includes whether it converged (`res.success`) and the optimal
parameters (`res.x`). Check both, always.

**A crucial experiment (in today's exercise):** start from several different
`x0` values. Same answer? For SSE the surface is a convex bowl, so yes —
unique minimum. Remember what that *buys* you; and remember that for wilder
objectives (module 09's GARCH likelihood, module 14's neural nets) the
surface is *not* a bowl, and starting points matter.

## 5. Constraints, in one picture

Real portfolios can't short (some), can't borrow infinitely, must sum to 1.
Constrained optimization = valley-walking *inside fences*. The optimum of a
constrained problem is generally NOT the unconstrained optimum — the fence
is binding. `minimize(..., constraints=[...], bounds=[...])` handles it;
day 12 does it properly for portfolios.

## 6. On real data

Today's exercise fits the market model
$R_{XLE,t} = a + b\, R_{SPY,t} + e_t$ by minimizing SSE numerically — and
compares to `statsmodels`' OLS (which solves the same problem in closed
form, day 11). If your numbers match to 4+ decimals, you have *earned* the
right to treat regression as a black box — because you've seen inside it.

## 7. Research connection

Every "we estimate the model by OLS" in the papers you will reproduce means
"we minimized SSE over the coefficients." Every "maximum likelihood" (GARCH,
Engle 1982) means "we maximized the probability of the data over the
parameters" — the same valley-walking, different surface. When module 09
fits GARCH and the optimizer reports convergence at a boundary, you'll know
exactly what that means, because today you watched `res.success` matter.

## 8. Common mistakes

- Not checking `res.success` / re-running from different starts — silent
  failure of the optimizer becomes a silent wrong number in a table.
- Minimizing the wrong objective: e.g., minimizing squared *prices* instead
  of squared *errors* (units matter; read your own SSE twice).
- Believing the optimum is meaningful if the surface is flat around it
  (many parameters give nearly the same SSE = the estimate is imprecise —
  module 06's "confidence interval" is exactly this idea, formalized).

## 9. Reflection

1. Why does squaring errors make regression sensitive to outliers? Design a
   one-sentence trading-research example where that sensitivity misleads.
2. What does it mean, intuitively, if minimizing from two starting points
   gives two different answers?

**Self-check:** state what least squares minimizes, why the squares, and why
a convex objective makes your life easy.
