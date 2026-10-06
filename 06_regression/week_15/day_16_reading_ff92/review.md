# Day 16 Review — Reading Fama & French (1992)

## Retrieval (answers)

1. FF92 design: FM monthly cross-sectional regressions, 1963–90;
   characteristics: portfolio-pre-ranked β, log size, BM (June t+1
   lagged), leverage, E/P.
2. Headlines: β slope ≈ 0/insignificant; size − (t ≈ −2.6), BM + (t ≈
   +4.4); joint: size & BM absorb β, leverage, E/P.
3. Absorption = day-9 attribution under correlation — observable across
   the univariate→joint columns; NOT a causal statement.
4. Knife 1: sample period (βs priced elsewhere/elsewhen); Knife 2: EIV
   attenuation — σ²_β/(σ²_β + σ²_eiv), portfolio binning divides σ²_eiv
   by ~bin size.
5. Table grammar: entries are average monthly slopes (%/month), t from
   step-2 slope scatter over T months; read univariate → joint → what
   died.

## Elaboration prompts

- "The absorption column cannot adjudicate between priors" — explain
  with worlds A and B, and name what COULD adjudicate (window/benchmark
  variation, longer samples, instrumented betas).
- Explain the June t+1 lag in one breath to someone who thinks it's
  pedantry. (Bankrupt firms' final filings predicting their own demise.)

## Interleaved problem

A 2026 working paper runs FF92-style FM on 2010–2025 and reports: BM
slope +0.05%/mo (t = 0.9), size slope ≈ 0, β slope +0.28%/mo (t = 3.1).
Twitter declares "value is dead, beta is back." Write the comment that
earns you a desk job.

<details><summary>Reference answer</summary>

"Nothing here is table-breaking; everything is PRIOR-updating. (i) A
15-year window has T ≈ 180 months — the BM slope's 95% CI spans roughly
−0.07 to +0.17%/mo, entirely consistent with a positive-but-smaller
premium (and with the factor's well-known 2007–2020 drawdown regime; the
λ̂_t ACF/share_pos rows would tell). 'Value is dead' on t = 0.9 is the
absence-of-evidence fallacy in public. (ii) β t = 3.1 with 15 years of
mostly-one-regime data (long bull, one crash) is exactly the
sample-period sensitivity FF92 taught — before celebrating, run the
split-period tables and the world-B check (does β's slope survive adding
momentum and quality, the characteristics KNOWN to correlate with
short-run β̂?). (iii) EIV direction reversed: β̂ estimated on 2-year
windows in a high-idio-vol decade attenuate size/BM MORE than β̂
(why? halved spread of true size/BM vs window-noise of β̂) — attenuation
favors whichever characteristic has the larger true cross-sectional
spike. Verdict: a fine period piece; re-run with rolling windows and
twenty more years before writing any obituaries, in either direction."
</details>

## Spaced repetition

- FF92 claims map (5 claims × evidence pattern): +1 week, redrawn.
- EIV attenuation formula + binning divisor: +1 month, re-derived.
- World A/B table prediction exercise: +3 months, on a fresh seed.

## Self-grade

- Could you read an unfamiliar FM table row-wise and column-wise, out
  loud, correctly?
- The June-lag firewall: can you build it into a pipeline? (Day 19 will
  ask.)
- Both obituary paragraphs: could you write them for a DIFFERENT factor?
