# Review — Probability Rules

## Retrieval

1. The union rule and why the subtraction term exists.
2. The pandas one-liner for P(A|B).
3. What does independence claim about conditionals — and what does it NOT
   say about squared returns?

<details><summary>Answers</summary>

1. P(A∪B) = P(A)+P(B)−P(A∩B); overlaps would otherwise double-count.
2. `A_mask[B_mask].mean()` — filter, then frequency.
3. P(A|B)=P(A); says nothing about dependence of |r| or r² — volatility
   clustering lives exactly there (day 19).

</details>

## Elaboration

- "P(strategy profitable | backtest profitable) can be small even when
  P(backtest profitable | strategy profitable) is large." Explain with
  base rates (preview of tomorrow).

## Spaced repetition

- Union/conditional rules return in module 04 (test logic) — restate the
  filter idiom at +1 week.
