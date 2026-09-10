# Day 4 Review — Skewness & Kurtosis

## Retrieval (answers)

1. ν = E[z³] (direction of the long tail); κ = E[z⁴] − 3 (tail weight
   vs normal). SEs: √(6/n), √(24/n).
2. One k-σ point in a sample of n contributes ≈ k⁴/n to κ̂ — kurtosis
   is an outlier detector: 20⁴/5000 ≈ 32.
3. Negative equity skew: leverage spirals (Black 1976); short-vol
   strategies harvest it in reverse (high win rate, negative skew).
4. QQ reading: symmetric fat tails (both ends curl), negative skew
   (left end only), S-middle (shoulders/data problems).
5. t(5) excess kurtosis = 6 — the workhorse toy for real daily returns.

## Elaboration prompts

- Your favorite strategy: sketch its P&L histogram's shape *from
  memory* of its worst months. What is its skew sign? What does that
  say about what it is short? (Every position is short something.)
- Kurtosis can't distinguish one catastrophic day from many bad days.
  Which do YOU fear more in a strategy you'd hold, and what statistic
  would measure that preference? (Crash clustering: the ACF of the
  bad days themselves.)

## Interleaved problem

Assets A and B, same σ = 1% daily. A: skew 0, κ = 8. B: skew −1.2,
κ = 3. You may hold ONE for a year with a −5% daily stop that, if hit,
costs an extra 1% slippage. Which do you choose, and what does each
shape predict about stop behavior?

<details><summary>Reference answer</summary>

B's long left tail (skew −1.2) means its big moves are concentrated in
the *down* direction — higher chance of a single gap through the stop
(−5% stop with −1% slippage on a fat left tail = the stop bleeds).
A's symmetric fat tails put equal mass on +and− extremes; its crashes
come as often from "normal" panic but with no directional
concentration. For a *stop-loss holder*, B is worse: negative skew is
a stop-loss machine's worst enemy (stops turn one −8% day into −6%
realized, but B's distribution makes those days systematically more
likely than A's). Rough ranking of stop-hit probability: B > A.
The deep point: equal σ, wildly different tail *mechanics* — σ is one
coordinate, not the map (day 10 says it again for vol).
</details>

## Self-grade

- k⁴/n from memory? QQ bend patterns?
- Can you compute t(5)'s kurtosis if asked tomorrow? (6/(ν−4) + ... —
  just know excess = 6/(df−4) for Student-t.)
