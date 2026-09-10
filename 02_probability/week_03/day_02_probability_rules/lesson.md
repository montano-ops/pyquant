# Day 2 — Probability Rules

## Warm-up retrieval (no notes)

1. Event vs sample space vs experiment — one sentence each.
2. Why is a realized return "one realization"?
3. What happened to your event-frequency estimate when the sample shrank?

## 1. Why a quant needs this

Every risk number, every signal-quality claim, every "this filter improves
win rate" pitch is arithmetic on probabilities. The rules are few and
simple; the mistakes are constant and expensive.

## 2. The three rules that do 95% of the work

**Complement:** $P(\text{not } A) = 1 - P(A)$. *Use:* a strategy wins 52%
of days → it loses-or-flats 48%. Stop-loss logic is complement arithmetic.

**Union (general):** $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$.
The subtraction prevents double-counting the overlap.
*Use:* P(spread > 1%) or P(spread < −1%) — "a big move in either
direction" = P(|r| > 1%).

**Conditional:** $\displaystyle P(A \mid B) = \frac{P(A \text{ and } B)}{P(B)}$
— "among the times B happened, how often did A?" The *workhorse of trading*:
P(win | signal fired), P(crash | vol spiked), P(reversal | gap down).

```python
import numpy as np
rng = np.random.default_rng(1)
r = rng.normal(0.0004, 0.011, 200_000)

A = r > 0.01                 # big gain
B = r > 0.005                # gain above half a percent (note: A implies B)
print(f"P(A|B) = {A[B].mean():.4f}")   # conditional = filter, then frequency
```

The code is the concept: **condition = filter the sample**. `A[B].mean()` is
literally P(A|B). Every "conditional backtest" you will ever read is this
filter — and every subtle bias in it comes from what that filter *does to
the sample* (module 05's survivorship is a conditioning you didn't ask for).

## 3. Independence — the assumption that powers everything (and fails quietly)

$A$ and $B$ independent $\iff P(A \mid B) = P(A) \iff P(A \text{ and } B) = P(A)P(B)$.

"B tells you nothing about A." Finance's canonical independence claim:
*consecutive daily returns are (nearly) independent* — the random-walk
hypothesis (day 16). Notice what independence does NOT say: it says nothing
about *squared* or *absolute* returns — real markets have near-independent
returns but strongly dependent *volatility* (day 19's whole point).

## 4. Two interpretations of probability (you use both, knowingly)

- **Frequentist**: long-run frequency — P(win) = fraction of wins in
  indefinitely many trials. The course's default for testing.
- **Subjective/Bayesian**: degree of belief, updated by evidence — day 3's
  Bayes rule. The honest frame for "how confident am I this edge is real?"

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")     # or synthetic
r = px["SPY"].pct_change().dropna()

up, big = r > 0, r > 0.015
print(f"P(up)        = {up.mean():.4f}")
print(f"P(big)       = {big.mean():.4f}")
print(f"P(up | big)? = ...")   # trick question — big implies up. P = 1.
```

Watch for logical implication (big ⊂ up): conditional probability of a
superset given the subset is 1. Sanity checks like this catch data and
logic bugs alike.

## 6. Research connection

Momentum papers condition on past returns: "P(next-month winner | past
winner) vs P(next-month winner)". The entire claim of JT93 is that these
conditionals differ — predictability is a *conditional* statement. And the
entire claim of market efficiency (day 16) is that they don't.

## 7. Common mistakes

- Double counting overlaps in unions (forgetting the −P(A and B)).
- Reading P(A|B) as P(B|A) — so important it gets all of tomorrow.
- Testing independence of returns and concluding "no predictability":
  independence of returns ≠ independence of |returns| (vol clustering —
  test both, always).

## 8. Reflection

1. Write P(strategy profitable | backtest profitable) in words. Why can it
   be tiny even when P(backtest profitable | strategy profitable) is large?
2. A signal fires on 2% of days. Explain with the complement rule why
   "the signal's false-alarm rate" and "the chance you're misled when it
   fires" are different numbers.

**Self-check:** state the three rules; then write the one-line pandas idiom
for a conditional probability.
