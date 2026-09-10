# Day 6 — Review: Days 1–5

Cold retrieval, then problems. Commit to answers before checking.

## Cold retrieval

1. raw_close vs adj_close vs auto-adjusted close — one line each,
   and what each is FOR.
2. The dividend factor (1 − D/P) and the split factor: what each does
   to PAST prices and why (units vs cash).
3. The CRSP return convention r_t = (P·S + D)/P_{t−1} − 1.
4. Dollar volume; Amihud illiquidity; the standard screens and the
   anomaly literature each screen distorts.
5. The join semantics (outer/inner) and why NaNs are preserved.
6. The four NaN-lattice patterns and their meanings.
7. The two return-from-panel bugs (phantom return; adjusted
   staleness).
8. BGI&R (1992): the mechanism, the mean effect, and the persistence
   effect.
9. The survivorship entry points table — all six rows.
10. The four cures, in order of strength.

## Interleaved problems

**P1.** A stock trades $100, pays a $4 dividend (ex tomorrow),
nothing else changes. Compute: raw return tomorrow; holder's return
tomorrow; the adjustment factor applied to today's price.

**P2.** Your panel has 30 stocks; 3 have leading NaNs to 2013, 2 have
trailing NaNs after 2020, 1 has interior NaNs (a halt week). Write
the panel_info table row for each pattern (what you'd report).

**P3.** A backtest: "universe = current DJIA members, 1990–2020,
equal weight, monthly rebalance, +2.1%/yr excess." Reconstruct the
three survivorship channels inflating the 2.1%, with directions.

**P4.** ADV screen at $1M: your signal is strongest in names with
$300k–$800k ADV. What is the honest report: the screened result, the
unscreened result, or something else?

**P5.** Why does `get_prices` raise on a failed ticker instead of
returning the ones it could fetch? Connect to a specific bias.

## Build (20 min)

From a blank notebook: build the 8-ticker panel (outer join), the
listing map (first/last/n/NaN%), returns with the phantom-return
check, and the panel_info table. Day 7 scales this to 50 tickers —
the drill is the engine.

## Error log

Days 1–5: which data-hygiene idea will you now apply to data you
already use? Log it concretely (the file, the check, the fix).
