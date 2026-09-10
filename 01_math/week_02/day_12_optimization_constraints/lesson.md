# Day 12 — Optimization with Constraints

## Warm-up retrieval (no notes)

1. Write the normal equations. What shape is $X^\top X$?
2. Why `solve` rather than `inv`?
3. What does the ones-column in the design matrix give you?

## 1. Why a quant needs this

Unconstrained optimization is a fantasy portfolio: weights of −340% and
+440%, "optimal" only if you can borrow infinitely at zero cost with no risk
manager. Real portfolio construction is optimization **inside fences** —
budget constraints, no-shorting, position limits, neutrality. Today:
constrained minimum variance, numerically, with `scipy`.

## 2. The problem

$$\min_{\mathbf{w}}\ \mathbf{w}^\top \Sigma \mathbf{w}
\quad \text{subject to} \quad
\mathbf{1}^\top \mathbf{w} = 1, \quad (\text{optionally } w_i \ge 0,\ \sum |w_i| \le L,\ \ldots)$$

- **Budget constraint** $\mathbf{1}^\top\mathbf{w} = \sum_i w_i = 1$: fully
  invested (the $\mathbf{1}$ is a vector of ones — its dot product with w is
  the sum).
- **Long-only**: $w_i \ge 0$ elementwise.
- **Leverage cap**: $\sum_i |w_i| \le L$ (gross exposure; $L = 2$ ≈ classic
  130/30 fund).
- (Module 11 adds *neutrality*: $\mathbf{1}^\top\mathbf{w} = 0$, beta
  constraints.)

## 3. The tool

```python
import numpy as np
from scipy.optimize import minimize

def min_var(Sigma, long_only=True):
    n = Sigma.shape[0]
    def obj(w):  return w @ Sigma @ w
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0}]
    bounds = [(0.0, 1.0)] * n if long_only else [(-2.0, 2.0)] * n
    res = minimize(obj, x0=np.full(n, 1 / n), constraints=cons,
                   bounds=bounds, method="SLSQP")
    assert res.success, res.message
    return res.x

w_mv = min_var(Sigma)                  # day 9/10's Sigma
print(np.sqrt(w_mv @ Sigma @ w_mv * 252))   # its annualized vol
```

Three craft habits: (1) start from equal weights — a *feasible* point;
(2) assert convergence, always; (3) after solving, **verify the constraints
yourself** (`w.sum()`, min(w)) — never trust the optimizer's word.

## 4. What you'll observe (the point of today)

- The **unconstrained-with-budget** solution wants big shorts in
  high-covariance assets and big longs in low-vol ones — mathematically
  optimal, operationally fictional.
- **Long-only** pushes weight into the lowest-vol assets (bonds, staples)
  and hits the bound $w_i \ge 0$ hard — the fence is *binding*: a
  constrained optimum is a different animal, not a nudged one.
- Small changes in $\Sigma$ move the optimal $\mathbf{w}$ a lot — the error
  maximization problem (module 09.17 formalizes; DeMiguel et al. 2009, your
  module 11 paper, is the definitive demo that naive 1/N often *beats* this
  optimization precisely because of it).

## 5. On real data

Today's exercise computes minimum-variance portfolios on your multi-asset
panel under three constraint regimes and compares: achieved vol, weights,
and stability of weights across two halves of the sample. The last one —
*stability* — is the professional's real question, because you must *trade*
into these weights, and turnover has costs (module 12).

## 6. Research connection

- **Markowitz (1952)** invented this problem; sixty years of practice
  discovered its fragility.
- **DeMiguel, Garlappi & Uppal (2009)** — your module 11 paper — compare
  optimized portfolios against 1/N across datasets and find the optimization
  edge is usually *smaller than its estimation error*. Today you feel the
  mechanism; module 11 reads the evidence.
- **Risk parity / vol weighting** (module 11) exists largely as a *robust*
  alternative: weights from vols only, no covariances to estimate badly.

## 7. Common mistakes

- Solving unconstrained and then "rounding" to feasible (not how it works —
  the constrained optimum is structurally different).
- Believing the optimized portfolio because the optimizer converged:
  convergence is math, not evidence. The objective's inputs ($\Sigma$,
  $\mu$) carry estimation error the optimizer *amplifies*.
- Forgetting the budget constraint and producing "weights" summing to 0.97 —
  silent 3% cash drag in every later calculation.

## 8. Reflection

1. Why does estimation error in $\Sigma$ get *amplified* by optimization?
   (Hint: the optimizer deliberately loads onto the entries that look best.)
2. Your minimum-variance weights differ wildly between sample halves. What
   does that imply about trading toward the "optimal" portfolio monthly?

**Self-check:** state the three constraint types from today and what each
means in trading terms; then explain why a binding constraint changes the
solution qualitatively.
