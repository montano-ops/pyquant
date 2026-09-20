# Day 11 Review — Outliers & Robustness: Winsorizing

## Retrieval (answers)

1. Trim = delete rows (holes in calendar); winsor = np.clip to quantiles
   (n and calendar intact; squared loss capped).
2. Buys: estimator stability (sd of β̂ down 15–35% in fat tails) and
   data-error containment. Costs: bias toward the calm-regime slope
   (~3–6% with t(4) tails) when tails carry signal.
3. The asymmetry: winsorize characteristics (measurement artifacts),
   never returns (tails = risk phenomenon). FF convention winsorizes x,
   not y.
4. Forbidden: winsor-for-significance ("until t > 2") — clip rule chosen
   ex ante, stated in methods, sensitivity disclosed.
5. Surgical removal beats indiscriminate clipping for provable bad prints
   (2% corruption survives a 1% clip half the time); deletions get logged
   by name in the data-quality report.

## Elaboration prompts

- "Winsorizing is an estimator with an opinion about the tails." What
  opinion, and when is it wrong?
- A risk manager wants the winsorized beta (smaller SE!) for a crash
  hedge. Explain — numbers from the tournament — why that SE is the calm
  beta's precision, not the crash beta's.

## Interleaved problem

Your market-model fit on a biotech: raw β̂ = 1.31 (SE 0.11); y-winsor
β̂ = 1.08 (SE 0.07); x-winsor β̂ = 1.30 (SE 0.11); D-check shows three
high-influence days, all FDA decision dates. The PM asks: "which number
goes in the risk system?" Compose the reply, including what you check
about those three dates first.

<details><summary>Reference answer</summary>

First check the three days against the data-quality standard: FDA dates
are real events with real prints (verify against a second source or
module-05 jump checks) — they're phenomenon, not prints. Winsorizing y
then erases exactly the event-driven information that defines a
biotech's market sensitivity (-23%: the E2 bias made visible), so its
smaller SE is precision about a world without FDA risk. x-winsor is
harmless but pointless (SPY's tails aren't the issue here). Risk system
gets **raw β̂ = 1.31 with its SE and the influence note**; the research
log gets the full table + dates + verification; and the spec gets a day-12
event-window treatment if FDA days recur often enough to interact
explicitly. "Which number" was the wrong question — which *regime* is the
system for?
</details>

## Spaced repetition

- The E2 tournament numbers (sd cut, bias): +1 month, re-derive by re-run.
- The clip-matrix (y vs x vs both vs delete): +3 months, redraw from
  memory with the dispositions column.

## Self-grade

- The credo sentence ("clip measurement errors, never the phenomenon")
  with one example each?
- The methods-paragraph structure (ex-ante rule, full fan disclosed)? cold?
- Can you name your OWN current analysis's three highest-leverage days?
