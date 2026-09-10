# Day 7 — Mini-Project: The Expectancy Simulator

## The brief

You know $\mathbb{E}[\text{P&L}] = pW - (1-p)L$. Today you *watch* it work —
and fail — through simulation, which is how researchers develop intuition
for the gap between expectation and experience.

**Build:**

1. A trade simulator: given (p, W, L, n_days, seed), generate a path of
   daily P&L: win +W with prob p, lose −L otherwise. (One `rng.choice` call.)
2. A distribution-of-outcomes viewer: for (p, W, L) = (0.55, 1%, 1%),
   simulate **1,000 one-year paths** (252 days each). Plot the histogram of
   *final wealth*; report the median, the 5th percentile, and the
   probability of ending below $1.
3. Repeat for (0.52, 1%, 1%) — the "slightly worse edge" — and for
   (0.55, 1.2%, 1%) — "same edge, asymmetric pay".

**Answer:**

- **Q1.** For (0.55, 1%, 1%): what fraction of years end in loss? The
  expectancy is clearly positive — reconcile the two facts using the
  variance of a sum and the $\sqrt{n}$ vs $n$ growth of signal vs noise.
- **Q2.** Going 0.55 → 0.52 changes the *mean* path by how much? Changes the
  *probability of a losing year* by how much? Which change would you notice
  first as a trader, and what does that imply about judging edges from
  experience?
- **Q3.** For the asymmetric-pay variant: does the losing-year probability
  match the symmetric one at equal expectancy? Explain via variance
  ($\text{Var} = p(1-p)(W+L)^2$ — derive or verify numerically).

**Reflection:** you have now *seen* that a genuinely positive-expectancy
strategy loses money over a year with non-trivial probability. Write three
sentences on what this does to your standards for "the backtest looks good".

Rules: fixed seeds; every random number traceable; histograms labeled;
state n for every reported frequency.
