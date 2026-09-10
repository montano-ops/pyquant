# Capstones — The Research Program

Six capstones, one per major paper family. Each is a **full research
project**: pre-registered question → data audit → methodology →
backtest → robustness → report. The nine notebooks in each folder are
the scaffold; [brief.md](01_momentum/brief.md) is the assignment;
[rubric.md](01_momentum/rubric.md) is the grade; `RESEARCH_LOG.md` is
your dated decision record.

## The sequence

| # | Project | Paper | After module | The skill it certifies |
|---|---|---|---|---|
| 1 | [Momentum](01_momentum/) | Jegadeesh & Titman (1993) | 07, 12 | cross-sectional sorting, portfolio legs, t-stats |
| 2 | [Reversal](02_reversal/) | Lehmann (1990) / Lo & MacKinlay (1990) | 08 | short-horizon predictability, microstructure suspicion |
| 3 | [Factor model](03_factor_model/) | Fama & French (1993) | 07 | time-series vs cross-sectional regressions, alpha vs beta |
| 4 | [Pairs trading](04_pairs_trading/) | Gatev, Goetzmann & Rouwenhorst (2006) | 09 | cointegration vs correlation, spread construction |
| 5 | [Volatility](05_volatility/) | Engle & Ng (1993) / GARCH family | 09 | vol modeling, risk-forecast evaluation |
| 6 | [Original research](06_original_research/) | yours | 13, 14 | the whole method, on a question you chose |

**Rule of order:** capstones unlock with their modules but never block
the next module. Momentum can start the week you finish module 07; the
original-research capstone starts only after module 13 (validation) —
starting it earlier is how people fool themselves professionally.

## The standard (identical for all six)

1. **Pre-registration first.** `01_question.ipynb` is completed and
   dated *before* `03_exploration.ipynb` runs. If reality forced a
   change, the change is in `RESEARCH_LOG.md` with a date — not silent.
2. **Data audit before models.** Survivorship, missingness, corporate
   actions — before any return is computed.
3. **Statistical ≠ economic ≠ tradable.** Every project ends with the
   three-way verdict: is the effect statistically real? economically
   meaningful net of nothing? tradable net of costs, capacity, and
   draws? Three separate answers, always.
4. **The bias audit is a deliverable, not a paragraph.** Each brief
   names the biases the design is most exposed to; the report must show
   the audit *run*, with numbers.
5. **The report is the product.** 4–8 pages in the
   [template](../templates/research_report.md); the backtest is just an
   exhibit in it.

## Grading

Each project has a 20-point rubric. **Below 16: fix the weakest
dimension before starting the next capstone** — the skills stack, and a
hole in project 1 is a chasm by project 6. The rubrics deliberately
reward honesty mechanisms (pre-registration, log discipline, reported
robustness failures) over headline Sharpe: **a validated null result
scores higher than an unexamined 2.0.**
