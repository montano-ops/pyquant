# Day 4 — Calculus I: Change and Sensitivity

## Warm-up retrieval (no notes)

1. Arithmetic vs geometric mean: which one does a backtest report owe the reader?
2. State the volatility-drag approximation.
3. How do you annualize (a) returns, (b) volatility — and why differently?

## 1. Why a quant needs this

You will never differentiate by hand in this course. You will *read*
derivatives constantly, because finance names them: **delta** (option price
vs underlying), **duration** (bond price vs rate), **gradient** (optimization
direction), **beta** (return vs market). All of these are
$\frac{d(\text{value})}{d(\text{driver})}$ — "how much does this thing move
when that thing moves?"

## 2. The derivative is a slope you already own

For $y = a + bx$, the slope is $b$ everywhere. For curved $y = f(x)$, the
slope differs by location; the derivative $f'(x)$ is the slope *at a point*:

$$f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}$$

Read it as: *"nudge x by a tiny h; see how much y moves; take the ratio."*
The limit is just "make the nudge as small as possible."

**Finite differences** — the computational version, no limit needed:

```python
def deriv(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h      # "nudge and look"
```

This is not a cheap trick; it is *the* method when $f$ is a pricing model, a
backtest, or anything you can only evaluate, not symbolize. Module 15
computes every Greek this way.

## 3. The three calculus facts you actually need

1. **Derivative of $a + bx$ is $b$** — linear functions have constant
   sensitivity. (Everything from day 2.)
2. **Derivative of $x^n$ is $n x^{n-1}$** — e.g., $\frac{d}{dx}x^2 = 2x$:
   the parabola's slope *grows* as you move away from zero.
3. **Second derivative = curvature (convexity).** $f'' > 0$: the function
   curves upward — "convex". Convexity is why option buyers survive crashes
   and why variance hurts compounding: $-50\%$ then $+100\%$ is
   convexity working against you (you end flat, not up).

## 4. Finance's derivative zoo (all the same animal)

| Quantity | is d(what)/d(what) | Use |
|---|---|---|
| beta | d(portfolio return)/d(market return) | exposure measurement, hedging |
| delta | d(option value)/d(spot) | option hedging (module 15) |
| duration | d(bond price)/d(interest rate) | rate risk (glance at module 15) |
| gradient | d(objective)/d(each parameter) | optimization direction (tomorrow) |
| marginal P&L | d(P&L)/d(weight) | portfolio sensitivity (module 11) |

## 5. On real data: the sensitivity of drawdown to one day

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2015-01-01")
r = px["SPY"].pct_change().dropna()
growth = (1 + r).cumprod()

# finite difference: how does final wealth change if day k's return is nudged?
def final_wealth(r_vec):          # f: return-path -> ending wealth
    return float(np.prod(1 + r_vec))

h = 1e-4
k = len(r) - 1                     # last day
perturbed = r.copy(); perturbed.iloc[k] += h
sensitivity = (final_wealth(perturbed) - final_wealth(r)) / h
```

The sensitivity of ending wealth to a tiny change in *today's* return is the
wealth level itself: $dW/d r_t = \prod_{s>t}(1+r_s)$ — nudges compound
through everything that follows. Small daily edges matter exactly as much as
your final wealth is large; that's the arithmetic behind "every basis point
counts."

## 6. Research connection

Volatility models (module 09) are statements about
$\frac{d(\text{risk})}{d(\text{time})}$ — how conditional variance evolves.
More immediately: when a paper says "the alpha estimate is sensitive to the
sample period", it means the *finite difference* of alpha with respect to
the window — the same "nudge and look" idea, applied to research itself.
Sensitivity analysis (module 13) is calculus with a security blanket.

## 7. Common mistakes

- Treating sensitivity as constant when the function is curved (delta of an
  option changes as the price moves — the second derivative matters).
- Confusing convexity (curvature, $f''$) with "leverage" (slope scaling).
  Convex payoff + zero slope still makes money in big moves.
- Numerical derivative with $h$ too large (you measure a chord, not a
  tangent) or too small (floating-point noise). $10^{-4}$ to $10^{-6}$ is
  the sane range for doubles.

## 8. Reflection

1. Why is "short volatility" a bet on convexity, not on direction? (Module
   15 will pay you to remember this.)
2. Give an example of a false conclusion from assuming constant sensitivity.

**Self-check:** define the derivative in words, name two finance aliases,
and say why finite differences are enough for this whole course.
