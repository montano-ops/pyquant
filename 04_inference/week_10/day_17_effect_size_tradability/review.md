# Day 17 Review — Effect Size vs Tradability

## Retrieval (answers)

1. The gate: NET = GROSS − COSTS, money units, per year. Inputs:
   gross, vol, events/yr, cost assumption (per round trip, at a
   stated size).
2. Death cost = per-event gross edge (μ_bp/events). Minimum viable
   cost at net Sharpe S: (μ_ann − S·σ_ann)/events.
3. Turnover is a property of the signal's persistence; cost is its
   tax — same signal, different rebalancing rule = different
   strategy, different verdict (the event-frequency trap).
4. Reversal's canonical shape: ~100bp/week gross, 52 events, 10bp
   kill-switch — the "real effect, dead trade" reference case.
5. The gate is necessary, not sufficient: a 5×-literate-magnitude
   edge that clears the gate is a data artifact until proven
   otherwise (the 04.12 warning).

## The two axes (the week's spine, complete)

> Axis 1 (the grill): is the effect real — SE design, power, family?
> Axis 2 (the gate): is the effect worth owning — costs, turnover,
> size? A strategy needs to clear both; most candidates fail at least
> one, and the two failures look nothing alike (a t-problem vs a
> cost-problem).

## Elaboration prompts

- Write the cost-gate paragraph (G5's structure) for a strategy you
  have actually backtested (even a toy) — every number in it must be
  traceable to a measurement or a stated assumption.
- Explain to a trader why "our Sharpe is 1.2" is an incomplete
  number: name the three missing inputs (cost basis, size, turnover
  rule) and the direction each one pushes the live number.
- A fund with 2bp access runs your 10bp-dead reversal. What changes
  in the gate, and what does NOT change (the signal, the vol, the
  turnover rule)? One sentence on who gets to trade what.

## Interleaved problem

Strategy C: gross 260bp/yr, vol 10%/yr, 12 events. Access: 6bp
round trip. (a) Net Sharpe. (b) Death cost. (c) The fund scales the
book 5× and impact doubles the cost to 12bp/RT: new net Sharpe, and
the one-sentence verdict change. (d) What gross edge at 12bp/RT would
restore the original net Sharpe?

<details><summary>Reference answer</summary>

(a) Net annual = 260 − 6×12 = 188bp/yr → Sharpe = 188/1000 =
**0.19**. (b) Death = 260/12 = 21.67bp/event. (c) net annual =
260 − 12×12 = 116bp/yr → Sharpe **0.12** — "alive, no longer
comfortable": the size change erased most of the edge without
touching the signal. (d) Need net_e =
15.67bp at 12bp cost → gross_e = 27.67bp → gross_annual = 27.67 × 12
= **332bp/yr** (+72bp, i.e., the signal would need a 28% bigger
edge to pay the same size tax). The general form: required gross =
original gross + Δcost × events.
</details>

## Self-grade

- Can you build the 5-cost grid for any (gross, vol, events) in under 3 minutes?
- Does your strategy card carry the gate's output, not the gross?
- Can you state the "event-frequency trap" example (same signal, two rules, opposite verdicts) from memory?
