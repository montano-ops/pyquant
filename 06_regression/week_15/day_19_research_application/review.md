# Day 19 — Review: Partial FF92 on Your Panel

**Time budget:** ~15 min the next morning; ~5 min on weekly review.

## The 90-second version

A complete cross-sectional study on a 50-name panel: three pre-declared
characteristics (trailing beta, log dollar volume, 12-2 momentum),
month-end information discipline with a printed shift audit, quintile
sorts + FM slopes, synthetic null AND positive controls gating every
conclusion, and a caveat table that prices proxy-quality, survivorship,
screen-truncation, skip-month, multiple-testing, and slope-ACF caveats
with direction and severity. The study's headline is allowed to be
"mostly nothing robust" — that IS the FF92-in-megacaps calibration.

## Retrieval practice (close everything first)

1. Why does momentum skip the most recent month (12-2 vs 12-1)?
2. What do the null control and the positive control each gate?
3. Name three caveats a 50-mega-survivor study cannot escape, with
   direction.
4. Your FM "size" slope is on ADV — say the honest comparison sentence
   to FF92.

*(Answers: (1) the skip month removes short-term reversal, which fights
momentum — 12-1 blends and can flip sign in reversal-heavy samples.
(2) null: |t| ~ <2.5 on un-planted chars or the pipeline has a bug →
stop; positive: planted +25bp/σ recovered within ~2 SEs or the test has
no power → stop. (3) Survivorship (+bias on risk-flavored premia; bound
≈1–2%/yr from module 05); screen truncation (slopes compressed toward
0 — size's habitat excluded); proxy (ADV ≠ cap → size slope confounded
with liquidity). (4) "My slope is not comparable in magnitude to FF92's
ME-slope — different regressor (liquidity proxy vs market cap),
different universe (screened megacap survivors vs all NYSE/AMEX) — only
the sign discipline and structure are comparable.")*

## If you had to re-derive one thing

The **accruals-level discipline of the three characteristics**: write
from memory, for each of beta / ldv / mom, exactly which dates the
inputs end on and which dates the response starts on, and the one-line
audit print that proves it. If you can't write the audit line cold, you
don't own point-in-time data yet — redo E1.

## Bookmark for module 06.21

This study is the FIRST independent research artifact; the checkpoint
(day 21) asks for its one-paragraph bottom line and table. Keep the
controls output, the joint FM table, and the caveat table — module 07
extends momentum from 12-2-suggestive to a priced factor; module 09's
delta method rewrites its SEs; module 13's backtest makes it strategy.
