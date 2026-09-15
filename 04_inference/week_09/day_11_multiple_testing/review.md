# Day 11 Review — Multiple Testing

## Retrieval (answers)

1. m null tests at 5%: E[V] = m/20; P(V ≥ 1) = 1 − 0.95^m
   (m=100 → 99.4%). One star out of 100 nulls is the modal noise
   outcome.
2. Bonferroni: each test at α/m → FWER ≤ α (union bound). Price:
   threshold 1.96 → ~3.6 at m=100; a real t=2.2 is now caught ~5% of
   the time. Right game for "one strategy, never wrong"; wrong game
   for mining.
3. BH: sort p's, largest k with p(k) ≤ kq/m, reject 1…k. Controls
   E[FDR] ≤ q under independence/most positive dependence. It manages
   a *set* of claims, not a single bet.
4. Zoo arithmetic: junk fraction among discoveries is set by family
   size m, not by the statistic. HLZ: with m ≈ 100+, t > 3 (not 2)
   keeps junk ~20–30% instead of 50–80%.
5. The core sin: reporting the best p over an uncounted search. The
   honest p is the minimum of m null p's — a mixture, much larger.

## Elaboration prompts

- In three sentences, explain to a skeptical fund CIO why "t = 2.1 on
  500 stocks" might be worthless, without using the word "multiple".
  (Family size; lottery; effective m.)
- When is Bonferroni the *right* answer, not just the safe one?
  (When you can afford only one true discovery and a false one is
  costly — e.g., funding a single live strategy — and the family is
  genuinely distinct hypotheses.)
- Your 40 variations are near-duplicates. Defend an effective family
  of 3 to a reviewer, in two sentences, using the test-statistic
  correlation as your evidence.

## Interleaved problem

You screen 200 candidate "factors" (correlations with next-month
returns, n = 1,200 months each, so SE(ρ̂) ≈ 1/√1200 ≈ 0.029).
(a) How many ρ̂ ≈ 0.05+ (|t| > ~1.7) should noise alone produce?
(b) You find 9 candidates with |t| > 2.0. Bonferroni-adjusted
  verdict? BH verdict at q = 0.05? (c) If the 9 have t's of
  {2.1, 2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 3.1, 3.4}, which would you keep
  as "real" under the HLZ logic, and what is your honest sentence
  about the rest?

<details><summary>Reference answer</summary>

(a) Null t's ~ N(0,1): 200 × P(|t|>1.7) ≈ 200 × 0.09 ≈ **18**
   candidates at t > 1.7 from pure noise. (b) Bonferroni at 200:
   threshold t ≈ 3.95 — none of the 9 survive; the family is almost
   certainly all noise. BH at q=0.05: sort the 200 p's; the 9 t's
   above are p's ≈ {0.036, 0.021, 0.016, 0.012, 0.009, 0.005, 0.0037,
   0.0017, 0.0007}; BH threshold at rank k is k·0.05/200 = 0.00025k —
   the smallest p (0.0007 at rank ~1) needs 0.00025: 0.0007 > 0.00025
   fails; typically **zero or at most one** rejection. (c) HLZ logic
   at m=200: keep t = 3.1 and 3.4 *as candidates* — still not
   "real"; they need replication, cost-adjustment, and economic
   plausibility. The honest sentence: "Of 200 screened, 9 exceed
   t=2 — which is *exactly* what noise predicts (200 × 0.0455 ≈ 9).
   The screen found nothing; t=3.1/3.4 are hypotheses to test out-of-sample, not
   out-of-sample, not discoveries."
</details>

## Self-grade

- Can you compute P(V ≥ 1) and E[V] for any m in your head?
- Can you implement BH in 10 lines and state its assumption?
- Did you write the "honest sentence" for a real screen, and does it
  count the family?
