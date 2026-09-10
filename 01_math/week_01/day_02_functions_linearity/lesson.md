# Day 2 — Functions and Linearity

## Warm-up retrieval (no notes)

1. Write the sample variance in Σ notation from memory.
2. What does `ddof=1` correspond to in the formula?
3. Translate $\prod_{t}(1+r_t)$ into one sentence.

## 1. Why a quant needs this

Almost every model in this course has the form $y = a + b\cdot x$: regression
(module 06), factor models (module 07), payoff diagrams (today), Greeks
(module 15). If you read $a + bx$ as slowly as you read a paragraph, every
later module slows down. Today you make it automatic.

## 2. The linear function, read fluently

$$f(x) = a + b x$$

- $b$ = **slope**: "when x rises by 1, y rises by b." Sensitivity. Exposure.
- $a$ = **intercept**: "where you start when x is 0." Baseline. Alpha-shaped.

Finance renames these constantly — that's the trick:

| Context | x | y | b | a |
|---|---|---|---|---|
| Market model (module 07) | market return | stock return | **beta** (exposure) | **alpha** |
| Payoff of holding 100 shares long | price | P&L | 100 (position) | 0 |
| Payoff with a $1 commission | price | P&L | 100 | −1 (friction) |
| Spread trade: long 1 unit A, short β units B | B's return | spread P&L | −β | hedge residual |

When a paper says "we control for market exposure", it means "we measured b
against the market and removed $b \cdot x$ from y." When it says "alpha", it
means: after accounting for the part explained by x, here is what remains —
*a*.

## 3. Payoff diagrams (finance's favorite linear functions)

Long 100 shares bought at $50: P&L(x) = 100·(x − 50) = 100x − 5000.
Short 100 shares: P&L(x) = −100x + 5000 — the mirror image, and the reason
shorting has *unbounded* downside: x has no ceiling.

```python
import numpy as np
x = np.linspace(30, 70, 100)          # possible prices
pnl_long, pnl_short = 100 * (x - 50), -100 * (x - 50)
```

Portfolio of linear payoffs = **sum of linear functions** = still linear.
This is why hedging works before options arrive (module 15 adds curvature).

## 4. Composition and the one nonlinear wrinkle you already know

Functions compose: fee(f(P&L)) — e.g., 2-and-20 fund fees are
$f(p) = 0.02 + 0.20\cdot\max(p - 0.02, 0)$: linear above the hurdle, flat
below. That $\max(\cdot,0)$ is a *hinge*, and it is your first nonlinear
object — it reappears as the payoff of every option in module 15.

Compounding is the other nonlinearity: wealth $W_t = W_0\prod(1+r)$ makes
wealth a *nonlinear* function of the return path. Today's takeaway: keep
clear which objects are linear (payoffs, exposures, weights) and which are
not (compounded wealth, fees with hurdles, option payoffs).

## 5. On real data: a first taste of "fitting a line"

```python
from qrc.data import get_prices
px = get_prices(["SPY", "XLE"], start="2015-01-01")
r = px.pct_change().dropna()
# a crude "beta": scale XLE's return by b = vol(XLE)/vol(SPY) and see how the
# daily P&L of "$100 in XLE" compares to "b·$100 in SPY" — day 11 does this properly
```

XLE (energy) vs SPY: clearly related, clearly not identical — a slope
awaiting measurement. Measuring slopes from data is *regression*; the
machinery arrives in module 06, but today's exercise builds the payoff
intuition it will sit on.

## 6. Research connection

Fama & French (1993)'s time-series regression is literally
$R_{it} - R_{ft} = a_i + b_i(R_{mt} - R_{ft}) + s_i SMB_t + h_i HML_t + e_{it}$
— four lines of the form you read today, one per factor, stacked. Every
"loading" ($b_i, s_i, h_i$) is a slope in the table above. When you reach
module 07 you will not spend a second decoding the notation — only debating
the economics.

## 7. Common mistakes

- Reading slope and intercept as "just numbers" instead of asking *what is
  the sensitivity, and what is the baseline* in this context.
- Forgetting that linear models are an **assumption**: real payoffs with
  fees, funding, and options are not linear; linear is the first
  approximation, and knowing when it breaks is the skill.
- Thinking "y = a + bx" is one object to memorize rather than a family to
  recognize under aliases (exposure, loading, delta, hedge ratio).

## 8. Reflection

1. Why is a hedge ratio a slope? What does the intercept of a hedged
   position's P&L represent?
2. Name one place where assuming linearity would produce a *false trading
   conclusion* (hint: think shorting, or fees, or drawdown-triggered flows).

**Self-check:** for the market model, state in words what beta and alpha
each measure — no symbols allowed.
