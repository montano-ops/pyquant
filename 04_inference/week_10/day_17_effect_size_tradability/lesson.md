# Day 17 — Effect Size vs Tradability

## 1. Warm-up retrieval (no notes)

1. The weekend effect: per-event edge, round-trip cost, annualized
   net. What was the verdict?
2. A t-stat says what about the effect's *existence* — and what
   does it NOT say about its *size*?
3. The detectable effect at 80% power, in SE units.

## 2. The gate

Every strategy in this course must pass the same gate before it
exists:

```
NET EDGE = GROSS EDGE − COSTS      (both in money units, per year)
```

Not "is the t big," not "is the premium positive" — *net of what it
costs to own, at the turnover it actually turns over, at a size that
fits its liquidity* (the last two arrive in module 12; today: the
first and honest skeleton of all three).

Three facts that make the gate do its work:

1. **Costs scale with turnover, not with the signal.** A 30bp/yr
   premium with 4,000%/yr turnover pays 40× more cost than the same
   premium with 100%/yr turnover. Turnover is a property of the
   *signal's persistence*; cost is its tax.
2. **The death cost is a number, not a vibe.** The per-event cost
   that zeroes the net edge — every strategy has one, and the
   strategy's future is argued against it (market making fees,
   spreads, impact, borrow).
3. **Significance and tradability are different axes.** t = 3.5 on a
   4bp/yr premium is "real and worthless"; t = 1.4 on a 900bp/yr
   premium with a tight CI is "not yet established and valuable."
   The grill (04.15) ranks the first axis; this day ranks the
   second. A strategy needs to clear *both*.

## 3. Intuition — the reversal lesson in one chart

Short-term reversal (Jegadeesh 1990; Lehmann 1990): 1-week losers
beat 1-week winners by on the order of 100bp/week gross — ~5%/yr at
full weekly turnover, with a t that is hard to argue with. The most
"significant" effect in the early anomaly literature. And its
turnover: near-complete, every week. At 10bp round trip, a 100bp/
week edge has almost nothing left; at realistic institutional costs
with impact, less. The effect is real — the trade is not. This is
the course's reference case for the gate: **the effect's magnitude
and the trade's viability are different objects, and the gap between
them is turnover × cost.** (Modules 10 and 12 build the reversal
strategy and its obituary in full.)

## 4. The mathematics

Per event (rebalance), with e events/year:

```
μ_e, σ_e : per-event mean, SD of the strategy's net-of-cost return
gross edge per event   μ_g
cost per event         c = 2 × cost_per_side  (round trip)
net per event          μ_e = μ_g − c
death cost             c* = μ_g              (net edge = 0)
min viable cost        c(S) = μ_g − S·σ_e     (net Sharpe = S per event
                                                on the per-event scale;
                                                equivalently on annual:
                                                c(S) = (μ_ann − S·σ_ann)/e)
```

Annualization: μ_ann = e·μ_g, cost_ann = e·c, σ_ann = σ_e·√e
(iid events). The Sharpe is annualization-invariant — as always.

**The cost grid.** For each strategy, the table that matters is
net Sharpe at c = 2, 5, 10, 20, 50 bp per round trip. A strategy
whose net Sharpe is positive at 50bp is robust; one that lives at 2bp
and dies at 10bp is a *market-maker's* strategy, not yours.

## 5. Python implementation

```python
import numpy as np

def gate(mu_ann_bp, sigma_ann, events, costs_bp=(2, 5, 10, 20, 50)):
    # sigma_ann in decimal (0.12 = 12%); returns (net bp/yr, annual Sharpe)
    out = {}
    for c in costs_bp:
        net_ann = mu_ann_bp - c*events
        sh = net_ann / (sigma_ann*1e4)
        out[c] = (net_ann, sh)
    death = mu_ann_bp/events
    viable05 = (mu_ann_bp/1e4 - 0.5*sigma_ann)/events
    return out, death, viable05

out, death, v05 = gate(900, 0.12, events=12)   # 900bp/yr, 12%/yr vol (0.12), monthly
for c, (net, sh) in out.items():
    print(f"cost {c:2d}bp/RT: net {net:+7.0f}bp/yr  Sharpe {sh:+.2f}")
print(f"death cost {death:.1f}bp/event | viable at Sharpe>=0.5 up to {v05:.1f}bp/event")
```

## 6. On real data

The gate is arithmetic, not data — but the *inputs* are data:
turnover from the signal's persistence (module 10 measures it), vol
from the strategy's own return series (module 12). Today you
practice on canonical numbers (momentum: ~900bp/yr, 12%/yr, 12
events; reversal: ~520bp/yr gross, 20%/yr, 52 events; factor tilt:
~300bp/yr, 8%/yr, 12 events); the exercise generalizes.

## 7. Research connection

- **Jegadeesh & Titman (1993):** "our results are robust to
  transaction costs of reasonable magnitude" — the paper's one
  sentence of cost honesty, and the standard since: state the cost
  assumption, show the net survives it. The gate formalizes what
  that sentence asserts.
- **Jegadeesh (1990) / Lehmann (1990):** reversal's gross magnitude
  and its turnover — the pair that makes "real effect, dead trade"
  a named category in the literature.
- **Moreira & Muir (2017), Corwin & Schultz (2012)** (module 10):
  cost *estimation* from free data (spread inference) — the day the
  c in your gate stops being a guess.

## 8. Common mistakes

1. **Gross Sharpe in the report, net in the margin.** The report
   shows gross; the live P&L is net. The gate's output — not the
   gross — is what goes in the strategy card.
2. **Cost as a fixed bp for all sizes.** 5bp/side at your backtest's
   size; 40bp at 10× size (impact, square-root law — 10.26/12.8).
   The death cost is *size-dependent*; state the size.
3. **Forgetting the long leg costs too.** Spreads tax *every* trade,
   long and short; borrow adds a *continuous* cost on shorts that
   doesn't fit the per-event model (module 12.4) — the gate's c
   understates the short side.

## 9. Reflection

- A strategy with 200bp/yr gross, 20%/yr turnover, at 5bp/RT: net
  positive. The same signal rebalanced *daily* (252 events): dead.
  The signal didn't change — the event frequency did. What does that
  say about what "the strategy" actually is? (It is the signal
  *plus* its rebalancing rule; the rule is part of the hypothesis.)
- The gate uses your *own* backtest vol for σ. If vol is
  underestimated (clustering — 04.9), the net Sharpe is
  overestimated. Which direction does the clustering bias push your
  *decision* to trade, and how big is the honest correction?

## Self-check

1. Gross 600bp/yr, vol 15%/yr, 252 events/yr (daily), 5bp round
   trip: net Sharpe; death cost.
2. Two strategies: A = 400bp/yr gross at 12 events, B = 1,600bp/yr
   gross at 252 events. Same vol (12%/yr), 10bp/RT. Which survives
   the gate, and why is the answer not "B has 4× the gross"?

---

**Answers:** (1) Net annual = 600 − 5×252 = −660bp/yr; net Sharpe =
−660/1500 ≈ **−0.44 — dead**. Death cost = 600/252 = 2.38bp/RT: the
strategy can afford less than 2.4bp round trip (the per-event view
says the same thing: 2.38bp gross vs 5bp cost). (2) A: 12×10 = 120bp cost → net 280bp/yr, Sharpe
≈ 280/1200 ≈ 0.23. B: 252×10 = 2,520bp cost → net −920bp/yr,
**dead**. A survives: the gate prices turnover, and "4× the gross"
is irrelevant when the cost tax is 6.5× higher. **The strategy is
the signal plus its rebalancing — B's daily rule is a different
strategy than B's monthly rule, and the dead one is the daily one.**
