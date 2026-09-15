# Day 12 Review — The Weekend Effect

## Retrieval (answers)

1. The three conflated claims: H1 Monday ≠ 0 (level); H2 Monday ≠
   other 4 days (contrast — the tradable one); H3 some day is special
   (the family). Audit all three; the trade lives on H2.
2. The 7-line audit: hypothesis → data/universe → method (design, SE,
   family) → result (contrast t + all raw t's) → stability → cost →
   verdict with caveats.
3. Placebo logic: run the same pipeline on data with a known-zero
   effect; the real result is judged relative to what noise produces.
4. Bonferroni over 5 days: α = 0.01 per test, t ≈ 2.58; BH(0.05)
   rejects the largest k with p(k) ≤ k·0.05/5.
5. Cost gate: break-even edge = round-trip cost per event (10bp);
   typical observed ~2bp → net ≈ −500bp/yr. Statistical visibility
   ≠ tradability.

## Elaboration prompts

- In two sentences, tell a friend why "Monday is negative" and "the
  Monday spread is negative" are different numbers with different
  t's — and which one you would trade.
- A paper reports the 1953–1980 effect as "robust" because it holds
  in 8 of 10 market samples. What is the family size in that sentence,
  and what would the audit require before you believe it?
- Write the E5 report line for a *synthetic* placebo run. (It should
  read almost exactly like the real-data report except the verdict —
  that similarity is the lesson.)

## Interleaved problem

Your own "anomaly": stocks with above-median weekend volume
(n = 2,400 stock-months) earn +6bp next Monday; the rest earn −1bp.
(a) Welch t on the contrast. (b) You also tested 4 other weekend
statistics (family = 5). Bonferroni verdict? (c) Round-trip cost 8bp.
Gross annualized if you rebalance every week; net. (d) One sentence
of verdict.

<details><summary>Reference answer</summary>

(a) SE = 1%·√(1/1200 + 1/1200) ≈ 0.041% (assuming SD ≈ 1% each,
n ≈ 1,200 each); t = 7bp/4.1bp ≈ **1.7**. (b) α/5 = 0.01 → need
t ≈ 2.58: **fails** — the family verdict is null. (c) 52 × 7bp =
+364bp/yr gross; 52 × 8bp = 416bp/yr cost; **net −52bp/yr** — dead.
(d) "A 1.7 t on one of five weekend statistics, negative after costs
at every realistic turnover — this is the 5% lottery wearing a
hypothesis costume; the honest disposition is a file, not a strategy."
</details>

## Self-grade

- Can you run the full 7-line audit unaided on any daily series?
- Did you compare the real result against the synthetic placebo, and
  say what that comparison does for you?
- Can you state the break-even rule (edge > round-trip cost per event)
  and compute it in 30 seconds?
