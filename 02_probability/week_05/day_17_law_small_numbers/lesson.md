# Day 17 — The Law of Small Numbers

## Warm-up retrieval (no notes)

1. Random walk in logs; two things it implies about variance.
2. What does EMH not claim?
3. What's the empirical signature of "efficient direction, predictable vol"?

## 1. Why a quant needs this

Today has one lesson and it's the most valuable in the module: **humans
systematically treat small samples as if they were large ones.** The name
is Tversky & Kahneman's (1971) — "belief in the law of small numbers" —
and it is the cognitive root of nearly every trading delusion: hot hands,
cold streaks, "the system stopped working", champion backtests, guru track
records. You now have the mathematics to be immune.

> Tversky, A. & Kahneman, D. (1971), "Belief in the Law of Small Numbers",
> *Psychological Bulletin* 76(2). Read pages 105–106 (the statement of the
> fallacy); the rest is optional.

## 2. The fallacy, stated

The *law of large numbers* is real: averages converge. The *belief in the
law of small numbers* is the error: expecting convergence to show up in
small samples — expecting a 55% process to *look like* 55% over 20 trades.
It won't. You computed the numbers on day 10:

| n | SE(p̂) at p=0.5 | A true 55% process shows |
|---|---|---|
| 20 | 0.112 | anywhere from 33% to 77% (95% band) |
| 100 | 0.050 | 45% to 65% |
| 1000 | 0.016 | 52% to 58% |

A 20-trade sample of a genuinely-better process is *indistinguishable* from
a coin flip — and a 20-trade sample of a coin flip regularly looks like a
guru (P(≥13/20 wins | p=0.5) ≈ 13%!).

## 3. The three trading faces of the fallacy

1. **The gambler's fallacy** (negative recency): "5 losses in a row — due
   for a win." Independence has no memory; the *dilution* of day 12
   happens, not compensation.
2. **The hot hand** (positive recency): "8 wins in a row — the system is
   on fire." Streaks of length L occur in fair coins with computable
   probability (the exercise computes them); with enough strategies
   tracked, spectacular streaks are guaranteed somewhere.
3. **Premature evaluation**: "I paper-traded it for a month and it works /
   it's broken." A month is noise (SE(p̂) ≈ 9pp); the evaluation window
   decides the conclusion, not the strategy.

## 4. The grinding-streaks simulation (do this once, remember forever)

```python
import numpy as np
rng = np.random.default_rng(21)

n_strats, n_days, p = 500, 250, 0.5
wins = rng.random((n_strats, n_days)) < p
rates = wins.mean(axis=1)
print(f"best of 500 coin-flip 'strategies' over 250 days: {rates.max():.1%}")
print(f"how many beat 55%: {(rates > 0.55).sum()} of {n_strats}")
```

Five hundred *coin flips tracked for a year* produce several "57% win rate
strategies" — pure selection over noise, orientation day 5's lesson with
today's machinery. Now add the behavioral layer: the tracking stops when
the manager *believes* (selection on belief, not on outcome) — and you have
the retail-guru industry explained in ten lines of numpy.

## 5. The remedy (what a researcher does instead)

1. **Pre-commit** the sample size and the evaluation rule before looking
   (module 13's pre-registration, in miniature).
2. **Compute the SE before computing the surprise**: an effect smaller
   than 2SE is not an effect, it's a draw.
3. **Demand n commensurate with the claim**: a claimed 1% monthly edge at
   4% monthly vol needs years of data to resolve (day 12's arithmetic; the
   t-statistic formalizes).
4. **Distrust streak narratives** — always ask "how many other streaks were
   possible and unobserved?"

## 6. Research connection

The multiple-testing crisis in asset pricing (Harvey, Liu & Zhu's "…and the
Cross-Section of Expected Returns" — module 13) is the law of small
numbers *at the scale of a literature*: hundreds of small-sample
"discoveries", each individually plausible, collectively riddled with
false positives. The t>3 threshold they propose is society's immune
response to today's fallacy.

## 7. Common mistakes

- Believing streaks need *either* skill or luck-as-explanation, when
  computation beats both.
- Asymmetry: noticing long win streaks (hot hand) but also expecting
  losses to reverse (gambler's fallacy) — the two errors coexist in the
  same brain, which is why you compute instead.
- "I'll just paper-trade to verify" with no n, no rule, no stopping
  criterion — evaluation theater.

## 8. Reflection

1. Your strategy won 8 of 10 months. Write the two-sentence reply you'd
   give a backer who wants to fund it now.
2. Where in *your own* behavior (be honest) does the law of small numbers
   most likely live? What computation would guard it?

**Self-check:** state the fallacy; reproduce the SE table from memory;
explain dilution vs compensation one final time.
