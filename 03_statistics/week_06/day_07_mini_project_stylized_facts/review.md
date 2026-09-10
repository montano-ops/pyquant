# Day 7 Review — Stylized-Facts Audit (mini-project debrief)

## Reference numbers (real data, 1993→ or 2005→; yours will vary by window)

| Fact | SPY (equity) | TLT (bond) | GLD (commodity) |
|---|---|---|---|
| 1. Excess kurtosis (daily) | 10–15 | 3–8 | 2–6 |
| 2. Max \|ACF(r)\|, lags 1–10 | ≲ 0.06 (inside band) | similar | similar |
| 3. ACF(\|r\|) lag 1 | 0.15–0.25 | 0.10–0.25 | 0.05–0.15 |
| 4. κ daily → weekly → monthly | 12 → ~3 → ~1 | 5 → ~1.5 → ~0.5 | 4 → ~1 → ~0.5 |
| 5. Leverage corr(r, Δlog vol) | −0.1 to −0.25 | ≈ 0 (bonds weaker) | ≈ 0 |
| 6. corr(\|r\|, volume) | +0.3 to +0.6 | similar | similar |

Verdict patterns: fat tails everywhere (fact 1 ✓ universal); no
directional memory (fact 2 ✓); vol memory weeks+ (fact 3 ✓);
aggregational gaussianity (fact 4 ✓ — κ collapses ~5–10× from daily to
monthly); leverage effect equity-specific (fact 5 — SPY yes, TLT/GLD
weak/zero — the audit's most instructive cell); volume-vol (fact 6 ✓
where volume is clean).

## The three tests your audit had to survive

1. **Window**: split the sample in half — do verdicts flip? (Fact 2's
   max ACF will poke past bands in *some* half by luck; kurtosis halves
   differ wildly — 2020 vs 2017.)
2. **Multiplicity**: 18 cells; at 2 SE, expect ~0.05 × 18 ≈ 1 "significant"
   result by luck. One marginal cell is noise, not a finding.
3. **Data quality**: volume series have their own artifacts (splits,
  vendor ffill) — a fact-6 verdict on bad volume data is a verdict
  about the vendor.

## Elaboration prompts

- Which fact disqualifies which model? Write the 3×3: normal-VaR
  (killed by fact 1), iid-simulation (killed by fact 3), GARCH-normal
  (survives 3, weakened by 1 — GARCH-t survives), constant-vol options
  pricing (killed by 3).
- Fact 5's asymmetry: check corr(r⁻, Δlog vol) vs corr(r⁺, Δlog vol) —
  negative returns should predict vol increases better than positive
  ones. Did they, in your data?

## What this project bought you

You now hold *measured* answers to "what's wrong with normal-iid
finance" — not folklore. Every time a paper, a tool, or a colleague
assumes thin tails or independent days, you can name the fact, the
statistic, and the size. That authority is the difference between
reading papers and reviewing them.
