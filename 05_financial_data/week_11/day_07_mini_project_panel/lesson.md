# Day 7 — Mini-Project: Research Panel v1

**The deliverable:** a 50-ticker research panel — adjusted and raw
prices, volume, corporate actions — plus the data-quality report that
makes it (and you) credible. This panel is the substrate for
capstones 1–5; the quality report is the habit.

## The build

1. **The universe**: `load_universe("research50")`. State what it IS
   (50 large US names alive today — a *survivorship-biased-by-
   construction* universe; day 5 taught you to say so out loud) and
   what research it can/cannot support (studies of liquid large caps;
   NOT population claims about stocks).

2. **The pull** (one pass, frozen): adj_close, raw_close, volume per
   ticker, 2005→ (or your choice — justify the start). Log the pull
   date. In synthetic mode: generate a 50-asset synthetic panel with
   staggered listing dates (the universe constructor: inject 5
   late-listers, 3 early-delisters, 2 with a halt gap, 1 with
   injected stale-zeros — the audit must FIND them).

3. **The panel**: outer join, NaNs preserved, returns computed with
   the phantom-return flag; listing map.

4. **The quality report** (the actual deliverable):
   - panel_info table: per ticker — first, last, n days, NaN%,
     n dividends, n splits, min price, median dollar volume, zero-run
     max, |r|>25% count.
   - The exception list: which tickers failed which check, and your
     disposition (verified-real / excluded-with-reason / fixed).
   - The NaN lattice heatmap (one figure, worth 1,000 words).
   - The three headline cross-checks: (a) split dates in actions vs
     jumps in raw close; (b) dividend dates vs adj/raw return gaps;
     (c) volume=0 days vs stale prices.

5. **The bias paragraph**: what this panel cannot see (the dead, the
   small, the illiquid, the foreign); the bounds you'd put on the
   survivorship content; which conclusions survive it (large-cap
   momentum: mostly; small-cap reversal: not).

## Method notes

- Automate every check — the report is code, not prose, so it
  regenerates when the panel updates. (The panel_info table is a
  DataFrame, printed.)
- A check that found NOTHING is still a check: print "0 exceptions"
  with the threshold stated. The report's value is its
  *reproducibility*, not its drama.
- Synthetic mode's injected defects are the grader: if your report
  doesn't find the 5 late-listers, the halt gap, and the stale
  series, the report is not yet a report.

## Self-assessment

- Could a stranger reconstruct your panel from your notebook in one
  run? (The test: rerun it. If it needs your memory, it's not done.)
- Did every exception get a disposition, or did some get silence?
- Is the bias paragraph specific to THIS panel (numbers), or
  boilerplate? Boilerplate is worth zero.
