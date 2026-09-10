# Capstone 2 — Short-Term Reversal (Lehmann 1990)

**The papers:** Lehmann, B. (1990), *Fads, Martingales, and Market
Efficiency*, QFA 25(1); Lo, A. & MacKinlay, C. (1990), *When Are
Contrarian Profits Due to Stock Market Overreaction?*, RFS 3(2).

## The question

Do weekly reversals (buy this week's losers, sell winners) earn real
returns, or is the "profit" the bid-ask bounce — a microstructure
phantom? H₀: spread = 0 after honest execution modeling.

## Required exhibits

1. The reversal spread: weekly, deciles, the contrarian return — with
   your best-effort SEs (overlapping weekly portfolios; module 08's
   variance-ratio logic is the formal cousin).
2. **The bid-ask autopsy**: decompose the spread into a "bounce"
   component (simulate execution at bid/ask vs mid) and the rest. The
   paper's punchline — most of it is bounce — is your target.
3. Lo–MacKinlay decomposition: autocovariance vs cross-autocovariance
   terms — is reversal within stocks or across stocks (lead-lag)?
4. Cost grid: reversal dies fastest of all strategies — at what round-
   trip cost does the spread hit zero? Compare that breakeven to
   plausible retail vs institutional costs.
5. Capacity note: reversal is small, fast, crowded — a one-paragraph
   estimate of the AUM at which your measured edge halves.

## The bias audit

Microstructure (the bounce IS the bias here), bid-ask bounce in the
*formation* return (ranking on noise), stale prices in losers
(module 03.12's trap), and the classic: weekly rebalancing demands
weekly liquidity — does your data's calendar survive the audit?

## Deliverables

Nine notebooks + report + three-way verdict. The headline you should be
proud of is not "reversal works" — it's a *measured* answer to "how
much survives honest execution," whichever way it lands.
