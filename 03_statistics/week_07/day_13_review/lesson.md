# Day 13 — Review: Days 8–12

Cold retrieval, interleaved problems, one cold-start build. Commit to
answers before checking review.md.

## Cold retrieval

1. The seven-step EDA liturgy, in order, with the question each answers.
2. The verdict-paragraph template (write it from memory — 5 sentences).
3. Rolling 63d mean of SPY: roughly what range? What does "negative 25–
   40% of the time" imply about regime claims?
4. The three explanations for mean instability.
5. Annualized vol: formula, assumption, and why it's a convention.
6. EWMA λ = 0.94: effective memory? Behavior after one 3σ day?
7. Vol's three blind spots.
8. JB formula and its two inputs' SEs; the big-sample pathology in one
   sentence; the small-sample mirror problem.
9. fillna(0) vs ffill(prices) — what does each lie about?
10. Aggregational Gaussianity: what it is, why it happens, the two
    directions of the scaling trap.

## Interleaved problems

**P1.** Weekly returns of a strategy: n = 260 (5 years), skew −0.3 ± ?,
kurtosis 2.1 ± ?. Compute the SEs; JB verdict; what would you do next?

**P2.** Asset A: daily σ = 1.2%, κ = 1. Asset B: daily σ = 1.2%, κ = 12.
Both at 20-day horizon for a 99% VaR: which has the bigger VaR, and
can you say by how much *without* the distributions? (Hint: you can
bound it, not compute it — say why.)

**P3.** Your 21-day rolling vol chart in March 2020 reads 80% annualized.
Your boss asks "so we might lose 80% this year?" — the three-part
correction.

**P4.** A backtest on a 30-stock panel uses `dropna()` and covers
2010–2020. List every sample-definition problem in one breath.

**P5.** Monthly Sharpe 0.9 (n = 60 months). The mean or the vol — which
is estimated more reliably? By roughly what factor? (SE comparisons —
the whole module in one line.)

## Cold-start build (20 min)

Blank notebook → your chosen asset → the full 7-step EDA with all
exhibits and the verdict paragraph. This is *dress rehearsal* for the
checkpoint: if any step takes more than 3 minutes, it's not yet yours.

## Error log + spaced repetition

- Book tomorrow's checkpoint: 90 minutes, closed everything.
- Queue the module's concepts into your spaced-repetition schedule
  (PROGRESS.md): SE price list, robust statistics, outlier protocol,
  aggregational Gaussianity.
