# Day 1 — Random Experiments, Outcomes, Events

## Warm-up retrieval (no notes)

1. Write the two-asset portfolio variance formula and point at the
   diversification term.
2. What does the equal-weight diversification curve converge to?
3. In OLS, what does the ones-column absorb?

## 1. Why a quant needs this

Statistics is the mathematics of *uncertainty about unknowns*; probability
is the mathematics of *randomness itself*. Before you can estimate anything,
you need a clean language for "what could happen" — because every dataset
you will ever touch is one realization of something random.

## 2. The vocabulary, built on trading

- **Random experiment**: a process with an uncertain outcome. *Tomorrow's
  return of SPY* is an experiment.
- **Sample space** Ω: every possible outcome. For a trading day, Ω is the
  whole real line of returns (practically, say −20% to +20%).
- **Event**: any subset of Ω you care about. "SPY gains more than 1%"
  ($r > 0.01$) is an event. "SPY is between −0.5% and +0.5%" is an event.
  Events are *questions about the future*, phrased as sets.

This reframing matters: the habit of research is to convert vague worries
("this strategy sometimes loses a lot") into measurable events
("P(daily loss > 2σ) = ?"). Probability theory is just bookkeeping for
events.

## 3. From outcomes to data: why "the return" is a random variable in waiting

Today's realized return (+0.7%) is *one draw* from the set of returns that
could have happened. The single most important mental shift in this course:

> You never observe "the market". You observe **one realization** of a
> random process, and every statistic you compute is a *summary of that one
> path* — not a measurement of the underlying truth.

This is why orientation day 5's champion strategy could look brilliant: you
saw one lucky path. It is why backtests need statistics at all.

## 4. Simulating frequencies: the researcher's grounding technique

Probability as long-run frequency can be *experienced* with simulation:

```python
import numpy as np
rng = np.random.default_rng(0)

n_days = 100_000
daily = rng.normal(0.0004, 0.011, n_days)          # a toy model of daily returns

event = daily > 0.01                                 # the event "gain > 1%"
print(f"P(gain > 1%) ≈ {event.mean():.4f}")          # frequency ≈ probability
```

Change `n_days` from 100k → 1,000 → 100 and watch the estimate wobble:
**probabilities estimated from finite samples are themselves noisy** — the
seed of module 04's entire existence.

## 5. Compound events (and the AND/OR bookkeeping)

- "gain > 1% AND volume above average" — intersection
- "gain > 1% OR loss > 1%" — union
- "NOT a gain" — complement

```python
A = daily > 0.01
B = daily < -0.01
print(f"P(A)={A.mean():.4f}  P(B)={B.mean():.4f}  P(A or B)={(A | B).mean():.4f}")
```

Notice: P(A or B) ≠ P(A) + P(B) — unless A and B are mutually exclusive
(they are here). The general rule arrives tomorrow.

## 6. Research connection

When a paper writes "the probability that the momentum portfolio loses more
than 10% in a month is 4%", that is an *event frequency measured on a
sample* — with sampling noise the paper usually doesn't display. When
risk-management reports "VaR₉₉ = 2.3%", it is "the 99th-percentile loss
event" (module 12 formalizes). Events are the atoms of every claim you will
evaluate.

## 7. Common mistakes

- Treating a realized number as the process ("SPY returns 0.04% a day"
  — no: it *did*; the process has a distribution).
- Defining events vaguely. "Losing a lot" is not an event; "r < −2%" is.
- Forgetting that simulated frequencies depend on the *model you simulated*
  — tomorrow's returns aren't normal; today's simulation is a toy.

## 8. Reflection

1. Define, as precise events: (a) a "crash", (b) a "crowded trade failing",
   (c) "the signal works". What makes (b) hard?
2. Your backtest shows 63% winning months over 5 years. Restate this as a
   statement about an event and a sample — what is the question you should
   immediately want to ask? (Hold that thought for three weeks.)

**Self-check:** experiment, sample space, event — define each with a trading
example, and say what "one realization" means.
