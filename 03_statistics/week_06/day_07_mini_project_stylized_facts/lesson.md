# Day 7 — Mini-Project: The Stylized-Facts Audit

**The paper:** R. Cont (2001), *Empirical properties of asset returns:
stylized facts and statistical issues* — the field guide every quant
claims to know and too few have actually run. Today you run it.

## The brief

For **three assets** — one equity index (SPY), one bond (TLT), one
commodity or single stock (GLD or XLE) — test Cont's facts and deliver
the audit table:

| Fact | Test | Statistic (± SE, n) | Verdict |
|---|---|---|---|
| 1. Heavy tails | excess kurtosis; QQ plot | k̂ ± √(24/n) | fat? how fat? |
| 2. No return autocorr | ACF lags 1–10 vs ±2/√T | max |ρ̂(k)| | inside bands? |
| 3. Vol clustering | ACF of \|r\| lags 1–10 | ρ̂(1), ρ̂(10) | outside? decay? |
| 4. Aggregational Gaussianity | kurtosis at daily/weekly/monthly | κ(d), κ(w), κ(m) | thinning? |
| 5. Leverage effect | corr(r_t, Δlog-vol_{t+1}) | ρ̂ | negative? |
| 6. Volume–vol | corr(\|r\|, volume) | ρ̂ | positive? |

## Method notes

- **Fact 4** resampling: weekly = non-overlapping 5-day sums; monthly =
  21-day. Use `.resample("W").sum()` / `"M"` — or `rolling().sum().iloc[::k]`;
  state your choice.
- **Fact 5**: rolling 21-day vol, log it, take *changes*; align with
  *same-day or lagged* returns (a choice — document it; Cont's asymmetry
  is the interesting part: negative returns predict vol better than
  positive ones).
- **Fact 6** needs volume: `get_prices(..., field="volume")`; if quality
  is doubtful, say so in the audit (data-quality checks ARE part of the
  deliverable).
- Every verdict carries its n. A fact "confirmed" on 250 days of data is
  a coin with paint on it.

## The deliverable (your notebook)

1. **The table**, three assets, six facts, statistics with SEs and ns.
2. **Three exhibits**: one QQ plot (pick the fattest-tailed asset), one
   |r| ACF, one kurtosis-vs-frequency bar chart.
3. **The paragraph**: you are the risk manager writing to the CIO —
   which model family is disqualified for each asset, and why, in plain
   sentences (e.g., "normal-VaR for XLE is disqualified by κ = 18 ± 1;
   iid simulation is disqualified for SPY by |r| ACF 0.22 at lag 1").
4. **The bias audit** (the course habit): survivorship (why SPY, TLT,
   GLD specifically?), window dependence (re-run on the second half of
   the sample — do verdicts flip?), multiplicity (18 tests; how many
   "significant" results would luck deliver?), and data quality (volume
   series, splits, the 2020 halt).

## Why this project is the course in miniature

Every later module is one cell of this table blown up to full size:
module 09 owns facts 1 & 3 (GARCH); module 08 owns fact 2's fine print
(variance ratios); module 05 owns the data-quality column; module 13
owns the audit. **Finish this day and you have personally reproduced the
empirical foundation that the entire quant literature stands on** — not
read it, not believed it: *measured it*.

Time-box: 90 minutes for the table, 30 for the paragraph and audit. The
solution is a full worked version with the reference numbers — compare
verdicts, not floats.
