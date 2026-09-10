# Day 14 — Checkpoint: Anatomy of a Distribution

**Your first formal research report.** Everything in modules 01–03 exists
to make this document possible. Closed notes, closed solutions; open
data, open code.

## The assignment

Choose an asset you have NOT analyzed this module (e.g., XLE, IWM, TLT,
GLD, a stock from the universe file — not SPY). Produce:

### 1. The data audit (before any statistic)

n, date range, source; missingness and calendar check; split/dividend
sanity (scan for |r| > 25% and verify against history — real or
artifact?); zero-return runs (stale data?); the one-paragraph data
verdict: "this series is/is not trustworthy because…"

### 2. The full EDA (day 8's liturgy, all seven steps)

Headline stats; histogram + QQ; skew/kurt **with SEs**; rolling mean &
vol; both ACFs; every exhibit titled and readable.

### 3. The statistics interrogation (the module's spine)

- Center: mean vs trimmed vs median — the three-way spread as a
  robustness finding.
- Spread: SD vs MAD-scaled — the gap as a fat-tail diagnostic.
- Tails: the |z|>3 tail multiple vs normality's 0.27%.
- Stability: rolling mean band vs its own SE — constant-μ consistent?
- The frequency cross-check: kurtosis daily vs weekly (fact 4).

### 4. The report

**≤ 400 words**, structured: Data → Distribution → Dependence →
Limitations → Recommendation. The recommendation names the model family
you would/wouldn't use for risk (normal? t? GARCH-t?) and one number
that justifies each verdict. Written for a risk manager who will act on
it — no hedging without a number.

### 5. The bias audit (mandatory section)

Which asset did you choose and why (selection)? Window sensitivity
(re-run headline stats on halves — do verdicts survive?)? What would
survivorship do to this asset's history (dead products, delistings)?
What did you test that luck could have produced (multiplicity)?

## Grading (self, honest)

| Dimension | Looks like | Points |
|---|---|---|
| Data audit catches real issues | you *checked*, not assumed | 3 |
| Every statistic carries (±, n) | the day-2 standard, no bare numbers | 3 |
| Exhibits answer questions | titled, readable, referenced in prose | 3 |
| Verdict paragraph is actionable | names models + numbers | 4 |
| Bias audit is specific | this asset, this window — not boilerplate | 4 |
| Statistical honesty | effect sizes over p-values; power mentioned | 3 |

20 points. Below 16: identify the weakest dimension and redo that
section tomorrow morning before opening module 04. The skill gap compounds
— this is the LAST module where the checkpoint is purely descriptive.

## Why "anatomy"

By now you should feel the shift: SPY is no longer "a ticker" — it's an
organism with a specific, measurable statistical anatomy: drift you can
barely resolve, risk you can forecast, tails that kill normal models,
dependence that punishes shufflers. **Every strategy you ever evaluate
is a claim about some asset's anatomy. You now know how to take the
measure of the body on the table.**
