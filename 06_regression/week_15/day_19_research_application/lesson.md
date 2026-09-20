# Day 19 — Research Application: Partial FF92 on Your Panel

## 1. Why a quant needs this

Everything this module taught was prefatory to this afternoon: a complete
cross-sectional study — characteristics vs future returns — on a panel
you built, with standard errors you can defend and caveats you've priced
before a referee finds them. This is FF92's skeleton at 1/50th scale
(50 names, ~15 years, no accounting data), which makes it also a lesson
in **what free data can and cannot support** — the honesty module 05
started.

## 2. The design (declare it all up front)

**Question.** In a 50-name megacap universe, do (a) trailing beta,
(b) liquidity/size proxy (log dollar volume), (c) 12-2 momentum predict
next-month returns?

**Why these three:** they're the only FF92-flavored characteristics free
data supports *honestly* — beta from returns (your day-7 machine),
liquidity/size from dollar volume (module 05), momentum from prices (the
JT93 preview — module 07 owns it fully). Book-to-market needs point-in-
time accounting data we don't have; **we say so, explicitly, and we do
not fake it.**

**Protocol (FF92-shaped):**
1. Characteristics at month-end t, computed strictly from data ≤ t:
   beta = trailing 252d rolling market beta; ldv = log median dollar
   volume over month t; mom = cumulative return months t−12..t−2
   (skip the most recent month — the 12-2 construction skips the
   short-term reversal window; write the reason in your log).
2. Response: month t+1 return. Non-overlapping months, shift audit
   printed.
3. Two readings: (i) **univariate quintile sorts** — mean next-month
   returns per quintile with the mean across months and its SE (a
   time-series test on the quintile portfolios — FM's simpler sibling);
   (ii) **FM slopes**, univariate then joint.
4. SE flavor: FM by construction; λ̂_t ACF check; slopes' NW if needed.
5. Synthetic mode: two controls — the null characteristics (machinery
   must NOT find premia) and one planted premium (machinery MUST find
   it). A study design that fails either control is rejected before data.

## 3. What you will find (and why it's the point)

In the real universe the headline is usually *nothing robust*: beta flat
(FF92 redux — inside a megacap-only universe, beta dispersion is
compressed), size/liquidity weak (the screen ate the dispersion — the
size effect's home is the excluded universe, module 05's screens table),
momentum the only flicker, and even that concentrated in a few regimes.
**The finding is the calibration**: within a survivorship-biased,
liquidity-screened 50-name megacap panel, FF92's structure shows the
megacap version of itself — mostly flat — and every "anomaly" headline
you ever read must be re-asked: *in which universe, measured how?*

The synthetic mode proves the machinery has power *when a premium
exists* (positive control) and doesn't hallucinate (null controls) —
report both, always. A methodology section that can't show a positive
control is asking to be taken on faith.

## 4. Common mistakes

1. **Proxy amnesia.** ADV is not shares outstanding × price; "size proxy"
   is not size; the measured size-slope mixes liquidity and size premia
   — label it, bound it, don't hide it.
2. **Skip-month omission.** Using 12-1 momentum (no skip) imports the
   one-month reversal — a different animal with opposite sign in many
   samples; JT93's skip is the discipline.
3. **Universe amnesia.** The report's scope line ("megacap survivors,
   2010–2026, USD") is not a footnote — it's the claim's boundary. Any
   sentence about "stocks" (full stop) is a lie your title slide tells.

## Self-check

1. Why 12-2 (the skip month)? What contaminates 12-1?
2. Two controls in synthetic mode — name each and the action it gates.
3. Three universe-level caveats this study cannot escape, with direction.

---

**Answers:** (1) The last month's return is dominated by short-term
reversal (microstructure + liquidity provision), which fights momentum;
skipping it isolates the continuation component. 12-1 blends the two
and flips sign in reversal-heavy samples. (2) Null control: un-planted
characteristics must slope ≈ 0 — finding "premia" there means the
pipeline is broken (stop); positive control: the planted premium must
be recovered within ~2 SEs — not finding it means the test is powerless
(stop). (3) Survivorship (universe = today's winners → premium estimates
biased positive for risk-flavored characteristics); screen truncation
(megacap-only → size/beta dispersion compressed toward zero slope);
proxy quality (ADV ≠ market cap → size slope confounded with liquidity
premium, direction ambiguous).
