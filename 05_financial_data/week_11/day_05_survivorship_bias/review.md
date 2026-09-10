# Day 5 Review — Survivorship Bias I

## Retrieval (answers)

1. BGI&R (1992): conditioning on survival selects on performance →
   survivor means overstate population means AND persistence tests
   overstate skill (survival correlates with winning streaks).
2. Mechanism magnifiers: death rate, performance-death correlation
   (strongly negative in reality), volatility.
3. Entry points: today's-index membership; fund databases (merged/
   liquidated excluded); rewritten index history; today's-cap lists
   applied backward; try/except ticker drops; vanishing vendor data
   for the dead.
4. Cures (strongest→weakest): point-in-time universes; include the
   dead with delisting returns (week 12); bound the bias by
   simulation; name it with numbers.
5. The qrc design lesson: loud failure on missing tickers — silent
   skips are survivorship by try/except.

## Elaboration prompts

- Run the graveyard demo with death-performance correlation −0.6 vs
   0 (same death rate). How much larger is the bias? The correlation
  is the villain — write the sentence.
- Find one published backtest (any blog/paper) using "current S&P
  500 constituents." Draft the two-sentence referee comment.

## Interleaved problem

Small-cap study: universe = stocks alive today with full 2005–2024
history, 8%/yr excess return. Death rate for small caps ~5%/yr;
dead stocks underperform survivors by ~4%/yr while alive; average
dead stock lives 10 of the 20 years. (a) Rough survivorship inflation
of the 8%? (b) The same study's momentum sub-result: is IT
inflated by the same channel, more, or less?

<details><summary>Reference answer</summary>

(a) The panel deletes ~5%/yr of the population whose realized returns
were ~4%/yr worse: each year, ~5% × 4% ≈ 20bp/yr of negative return
vanishes — plus the compounding asymmetry (the dead's worst final
year — the death year, typically −30 to −80% — is entirely absent).
Honest range: 0.5–1.5%/yr of the 8% is survivorship — the premium
is real but smaller, and its tail is truncated (the dead's deaths
would have added left-tail mass the study never sees).
(b) Differently — and the net sign on a long-short is NOT obvious,
which is the point. Two channels pull opposite ways: (i) the long
leg never holds a winner's terminal collapse (winners that later
die are absent) — inflates the long leg; (ii) the short leg's best
trades ARE the dying losers' terminal collapses (the −30%
delisting months) — absent, so the measured short leg is too kind
— deflates the spread. In small caps deaths concentrate in the
short leg (near-delisters are recent losers), so the net effect on
the spread is likely DOWNWARD — the honest momentum premium is
bigger than the survivor study shows — while the long-only level
is overstated and any persistence claim ("winners keep winning",
BGI&R) is manufactured upward: survival correlates with the very
streaks being measured. **Survivorship is not a uniform tax — it
concentrates in the tails, in strategies that touch the dying, and
it can distort long and short legs in opposite directions.**

</details>

## Self-grade

- The mechanism sentence, verbatim-cold?
- All six entry points named?
