# Day 7 — Mini-Project: First Contact

## The brief

Your first complete research cycle, in miniature. Three assets, five
questions, one page of writing. Everything here uses only what you learned
this week — that's the point: prove the week compiles.

**Data.** SPY (US large-cap equities), QQQ (Nasdaq-100), GLD (gold), daily,
2010-01-01 to the most recent date (or the synthetic trio if offline — say so
in your write-up; it changes the *numbers*, never the *method*).

**Compute.** Daily simple returns; annualized volatility; cumulative growth
of $1; maximum drawdown, defined for now as the largest peak-to-trough decline
of the $1 growth series (find it with a rolling max: `growth / growth.cummax()
- 1`, then take the min — the solution shows one clean way).

**Answer (Q1–Q5), each in 2–4 sentences plus any numbers/plots:**

- **Q1 — Ranking.** Which asset had the highest return? The highest
  volatility? The worst drawdown? Is "highest return" the same asset as
  "best investment"? Why not?
- **Q2 — Signal vs noise.** For SPY, compare the size of the average daily
  return to the size of daily fluctuations (std). Roughly how many "signal"
  units fit inside one "noise" unit? What does that say about judging a
  strategy by a few months of returns?
- **Q3 — Symmetry.** Are daily returns roughly symmetric up/down? Count days
  above/below the mean; look at the largest gain vs largest loss. Note
  anything asymmetric — you'll formalize this as *skewness* in module 03.
- **Q4 — Volatility over time.** Plot the 63-day rolling annualized
  volatility for each asset. Is volatility constant? Does it cluster in calm
  and stormy periods? What does "constant vol" as an assumption imply?
- **Q5 — Correlation.** Compute the correlation of daily returns between the
  three assets. Which pair is most correlated? What happens to diversification
  if correlations rise in crises (check: correlation computed only on SPY's
  20 worst days)?

**Write the data diary (one page):**

- Header: date, data source, `DATA_SOURCE` mode, sample period actually used.
- Answers Q1–Q5 with figures where useful.
- **Bias audit lite:** What could make your conclusions wrong? Consider at
  least: sample-period choice (would 2000–2010 change Q1? you don't need to
  run it — reason about it), survivorship (do these ETFs survive *because*
  they're famous? what's missing from a 3-ETF universe?), and costs (you
  ignored them — for what strategies would that be fatal?).
- **Reflection:** the four standard questions (what did you learn / what does
  this method assume / how could it mislead / what would you test next).

**Rules of engagement for projects (from now on):** work the questions in
order; write your answers *before* opening the solution notebook; then
compare and log differences in your error log. The solution is an exemplar,
not an answer key — your numbers will differ if your sample differs, and
noticing *why* is itself learning.

## What "done" means

You can defend every number you report ("this is 252 × the mean daily log
return" / "this is a mean of simple daily returns × 252 — and here's why I
chose it"), and your bias audit contains at least one way your own conclusion
could be wrong that you found *yourself*.
