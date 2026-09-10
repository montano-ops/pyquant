# Day 6 Review — Week-11 Consolidation

## Cold retrieval (reference answers)

1. raw (as-traded, execution/sizing) · adj (raw × cumulative factor,
   total return, backtests) · auto-adjusted (split-only). Never mix
   pulls across dates.
2. Split: past ÷ ratio (units). Dividend: past × (1 − D/P) (cash).
   CRSP: r = (P·S + D)/P_prev − 1. Unit test: constant ratio to
   provider; identical returns.
3. Amihud = mean(|r|/DV); screens (price/ADV/history/exchange) each
   select away a literature; volume-vol corr +0.3–0.5.
4. Outer join, NaNs preserved: leading = pre-IPO, trailing = delist,
   interior = halt/gap, all-NaN = failure (loud). dropna(panel) =
   survivorship via cleaning.
5. Phantom return (gap-crossing pct_change) and staleness (mixed
   pulls) — flagged/frozen respectively.
6. BGI&R: survival-conditioning inflates means AND manufactures
   persistence. Magnifiers: death rate × dead-gap × vol.
7. Cures: point-in-time; include the dead (delisting returns, wk 12);
   simulate bounds; name it with numbers.
8. panel_info: first/last/n/NaN%/actions/min price/median DV/zero-
   runs/|r|>25% — the ID card at the top of every notebook.

## Interleaved problems (reference answers)

**P1.** Raw return: −4%; holder: 0% (cash received); factor on past:
×(1 − 4/100) = 0.96.

**P2.** Late-lister: first=2013, leading NaNs, note "IPO 2013 — not
missing, nonexistent." Early-delister: last=2020, trailing NaNs,
"acquired — delisting return needed (week 12)." Halter: interior gap
of 5, "halt — phantom-return flag on resumption day."

**P3.** (1) Dead members absent (their 2008 losses deleted); (2)
post-2009 entrants present from their good years (membership earned
by rally); (3) equal-weight rebalancing INTO survivors' recovery,
unopposed by the deleted dead. Net: 2.1%/yr is plausibly 0.6–1.2%/yr
of pure construction.

**P4.** Report BOTH, plus the honest third thing: the signal's
strength-by-bucket with costs, and the capacity of the sub-$1M bucket
(~0) — "the effect is real and mostly untradable" is a finding, not a
failure.

**P5.** Silent skip = survivorship by try/except: the missing ticker
is disproportionately dead, and dead correlates with losing — the
pipeline deletes losers mechanically. Loud failure forces a universe
DECISION (documented, bounded) instead of an accident.

## Build check

The 8-ticker panel drill in 20 minutes: outer join, listing map,
phantom flags, ID card. Day 7 is this ×50 with the quality report —
if the drill needed your memory, fix that first.
