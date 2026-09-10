# Day 5 — Survivorship Bias I

## 1. The paper

**Brown, Goetzmann, Ibbotson & Ross (1992), *Survivorship Bias in
Performance Studies*, RFS 5(4).** The question: how much does
measuring performance on *existing* funds overstate the population's
performance? Their setting: mutual funds, where the dead (merged/
liquidated) are excluded from the standard databases — and the dead
underperformed while alive. The headline: survivorship can add
materially to measured mean returns, and — the subtle point — **it
biases persistence tests toward finding skill** (winners survive;
so winning streaks are over-represented), which fed directly into the
hot-hands debate of the 1990s.

The mechanism, stated once, used forever:

> **Conditioning the sample on the outcome (survival) selects on
> performance, so measured past performance of the survivors
> overstates the population's.**

## 2. The delisted demo

```python
from qrc.universe import load_universe
print(load_universe("delisted_demo"))
```

Six names that once sat in major indices. **LEH** (Lehman Brothers)
went to ~zero in 2008 — but LEH is *not in the S&P 500 today*, so
**any backtest whose universe is "today's S&P constituents" doesn't
contain Lehman's death**: 2008 is reconstructed as a market where the
companies that failed simply... weren't there. The bankrupt are
erased; the rebalanced survivors' subsequent rally is kept.

**Run it (online):** fetch `LEH` raw closes ending 2008, `TWX`,
`CELG`, `MON`, `AGN` — all acquired (holders got cash or shares —
those returns exist in a proper database and are MISSING from
today's-list panels).

## 3. Quantify it yourself (offline-safe)

Module 03.1's graveyard demo is the model: simulate 200 funds, kill
the bottom 30% mid-way, measure the survivors-only average vs the
truth. Parameters that control the damage:

- **Death rate** (how many die).
- **Correlation between performance and death** (the killer: funds
  don't die at random — they die BECAUSE they lost).
- **Volatility** (more vol → more selection range).

In markets the correlation is strongly negative (losers die), so the
bias is close to its worst case: **today's-list universes
overstate mean returns by roughly the death rate × the dead-vs-alive
performance gap.** With ~5%/yr disappearance for small stocks and
dead-underperformance of several percent, 0.5–2%/yr of "excess
return" in small-cap studies is plausibly pure survivorship — the
size premium literature's running argument.

## 4. Where it hides (the map for your own work)

| Backtest ingredient | Survivorship entry point |
|---|---|
| "S&P 500 stocks" | today's membership, not point-in-time |
| ETF/fund databases | merged/liquidated funds excluded |
| index histories | rewritten after recompositions |
| "top 100 by market cap" | computed on TODAY's caps, applied backward |
| your own try/except loops | dropped tickers are dead tickers |
| price data availability | dead tickers' data vanishes from vendors |

The last row is the quiet one: **a ticker that no longer exists often
returns no data — and code that skips it ("couldn't fetch, moving on")
writes the bias into the pipeline mechanically.** That's why
`qrc.data.get_prices` raises on failure instead of continuing: loud
failure beats silent bias.

## 5. The cures (partial, always)

1. **Point-in-time universes**: membership as it was ON THE DATE
   (needs a historical-constituent source — the professional
   requirement; free sources rarely have it).
2. **Include the dead** (CRSP-style: delisting returns included —
   week 12's day 05.8 does delisting returns properly).
3. **Bound the bias**: simulate the graveyard (§3) with plausible
   parameters and report the range — "if disappearance were X% and
   dead underperformance Y%, the measured premium shrinks to Z."
4. **At minimum: say it.** A limitations paragraph that quantifies
   nothing is worth little, but a paper that doesn't even name the
   issue has told you its data hygiene.

## 6. The BGI&R subtlety, in your words (write it)

Survivorship doesn't just inflate levels — **it manufactures
persistence**: "winners keep winning" is partly "winners survived,
and survival correlates with past winning." Before you accept any
hot-hands/momentum-in-funds evidence, ask: was the sample selected on
survival? (This is also the answer to "why does my fund's backtest
show manager skill": managers whose losing funds died are not in the
sample.)

## Self-check

1. Your universe: "current Nasdaq-100 members, 2005–2025." List three
   distinct ways 2008–2012 returns are overstated.
2. Why does survivorship bias *persistence tests* more than mean
   returns, per BGI&R?
3. A database with no dead funds advertises "no survivorship bias —
   we include all funds ever." Two follow-up questions.

---

**Answers:** (1) Members that failed/were removed (dead) absent;
rebalanced-in winners (post-2009 entrants like NFLX-era membership)
present for the rally they earned membership WITH; market-cap-based
signals computed on today's caps select the survivors backward.
(2) Because survival itself is caused partly by past returns — the
sample over-represents return-persistence *by construction*; means
are inflated by the dead's absence, but persistence is inflated by
the selection being correlated with the very streaks being measured.
(3) (a) "Including all funds ever" usually means all funds ever
*recorded* — backfill: when did each fund ENTER the database (many
enter only after good performance — incubation/backfill bias)?
(b) Are delisting/liquidation returns included at the event, or do
series just stop (stopping mid-track silently deletes the final,
worst months)?
