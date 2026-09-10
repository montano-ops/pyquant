# Capstone 4 — Pairs Trading (Gatev, Goetzmann & Rouwenhorst 2006)

**The paper:** Gatev, E., Goetzmann, W. & Rouwenhorst, K. (2006),
*Pairs Trading: Performance of a Relative-Value Arbitrage Rule*,
Review of Financial Studies 19(3).

## The question

Does trading converged-then-diverged pairs (long the loser, short the
winner, bet on re-convergence) earn returns that survive costs — and is
the "convergence" cointegration or mere correlation?

## Required exhibits

1. Pair selection: minimum-distance matching over formation (the
   paper's Σd² criterion) on your universe; how many pairs survive.
2. Spread construction and trade triggers (2σ divergence → enter,
   re-converge or time-stop → exit); the full P&L simulation at
   portfolio level.
3. **Cointegration vs correlation**: for your best and worst pairs,
   test properly (module 09's tools; correlation + intuition if you
   precede it) — show a pair that correlates but doesn't converge and
   what the strategy does with it.
4. Cost and shorting reality: entry/exit costs, borrow availability;
   the breakeven cost per round trip.
5. The crowding decade: performance by sub-period — pairs famously
   decayed as the trade became known; is the decay in your data, and is
   it statistically distinguishable from noise (module 04's machinery)?

## The bias audit

Selection of pairs on in-sample convergence (the strategy is long
"pairs that already behaved" — the graveyard of dead pairs is
invisible), the doubled look-ahead risk (formation AND trigger windows),
shorting costs, and the period-dependence of the headline.

## Deliverables

Nine notebooks + report + verdict. The transferable skill: relative-
value logic — spread construction, entry/exit states, and the humility
that a stationary-looking spread is a *hypothesis*, not a fact.
