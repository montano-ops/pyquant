# Day 16 — Reading Fama & French (1992)

## 1. Why this paper, on this day

You have every tool the paper uses: day 15's Fama–MacBeth is its
statistical engine; day 9's collinearity is its central table's grammar;
day 3's SEs are its error bars; module 05's bias audits are how its
authors slept at night. Fama & French (1992) asked the cleanest question
in asset pricing — *what, in the cross-section of stocks, is related to
average returns?* — and answered with an FM table that *changed the
field's mind about beta*. Reading it properly is a rite of professional
passage; today you read with attack eyes.

## 2. The paper in one breath

Sample: NYSE/AMEX/Nasdaq, 1963–1990. Design: FM monthly cross-sectional
regressions of returns on characteristics — pre-ranked **β** (estimated
on portfolios pre-formation; the EIV defense you'll test today), **size**
(log ME), **book-to-market** (BM, accounting data lagged into June of
year t+1 — the point-in-time discipline), leverage, E/P. Findings that
print on the back of the field's jersey:

1. **β, alone, is ≈ flat** in 1963–1990: the univariate FM slope on β is
   near zero and insignificant (whereas earlier samples — Black, Jensen &
   Scholes 1972 — had found it positive).
2. **Size (−) and book-to-market (+) price returns**: FM t's of ≈ −2.6
   and ≈ +4.4. Small and "cheap" beat big and "expensive".
3. **Absorption**: in joint FM regressions, size and BM *absorb* β,
   leverage, and E/P — their slopes die; size/BM's survive.

Claim 3 is a multicollinearity sentence (day 9): characteristics that
correlate with each other enter one regression, and the slopes with the
stronger joint information survive. It is a finding about *this data's
ability to attribute*, as much as about the world.

## 3. Reading the table's grammar (Table II/III forms, universal since)

- Rows = characteristics; columns = which subset is included (univariate
  first, then joint) — the absorption drama plays across the COLUMNS.
- Entries = average FM slope in %/month, t-stat in parentheses, from the
  step-2 series — **now you know what that means**: a mean of monthly
  cross-sectional slopes over T ≈ 330 months, SE from the slope scatter.
- Read in this order: (i) univariate column for each characteristic (does
  it price alone?); (ii) the joint column (does it survive company?);
  (iii) per row: what *died* when the row's friends entered — that's the
  collinearity story; (iv) magnitudes, not just t's: %/month × economic
  meaning ("−0.15%/σ of log size" ≈ small-minus-big ≈ 1.8%/yr per σ).

## 4. The worked miniature (what your exercise reproduces)

Two constructed worlds, both with N = 100 names, T = 240 months:

- **World A (FF92's world):** returns pay only size (−) and BM (+); true
  β premium ≡ 0. FM tables: univariate β-slope ≈ 0; joint: size/BM
  significant — the paper's headline pattern emerges *because the DGP
  said so*. Lesson: the table pattern RR — flat β, priced size/BM — IS
  what such a world looks like.
- **World B (β's revenge):** returns pay β (+), and β correlates with
  size−/BM+ (small names are high-beta). Univariate columns: size and BM
  "price" returns! Joint: β's slope survives, theirs collapse — the
  mirror-image pattern. Lesson: **"absorption" is attribution under
  correlation;** the same arithmetic that made FF92's table would, in
  world B, falsely bury beta. The data alone cannot always say which
  world you're in — that's (one) reason the debate ran 30 years.

## 5. Reading with charity and with a knife

- **Charity**: doing this in 1992 meant hand-built point-in-time
  accounting panels and honest FM machinery; the paper's negative result
  (against CAPM, by its friends) is the field's best self-correction
  story.
- **Knife #1 (sample period)**: β priced pre-1963, flat 1963–90. One
  interval's flatness is not a law; the later FF papers themselves
  re-found market-beta priced where it should be (when the market is the
  market portfolio and risk is measured right).
- **Knife #2 (EIV)**: β̂ is *estimated*; errors-in-variables attenuate
  its slope toward zero exactly when other characteristics correlate
  with the estimation error. FF pre-ranked on portfolios to shrink EIV —
  your E3 tests how much that helps. Shanken's critique (1992) is this,
  formalized: *the "death of beta" is partly a measurement statement*.
- **Practical upshot for your desk life:** "does X predict returns?" is
  always asked against a background of correlated characteristics; the
  univariate/joint column discipline — and world-B counterfactual
  thinking — is the reading skill.

## 6. Common mistakes

1. **Quoting "β is dead" as a theorem.** It's a sample-period FM slope
   with an SE, in a design with estimated betas. Module 07.3 shows the
   longer-run evidence.
2. **Reading absorption as causation.** Size absorbing E/P doesn't make
   E/P "not matter"; it makes E/P's *independent* information
   indistinguishable from size's at this n and correlation.
3. **Forgetting the June t+1 lag convention** when reproducing: matching
   accounting year-t data to July-t+1→June-t+2 returns. Skip the lag and
   you let bankrupt companies' last reports predict their demise from
   beyond the grave — look-ahead in its Sunday suit.

## Self-check

1. List FF92's three headline findings and name the table-structure
   (columns) where each lives.
2. Why is absorption a day-9 fact? Give the one-sentence mechanism.
3. Two critiques of "β is flat" that are about measurement, not theory —
   and the design element of FF92 that partially answers the second.

---

**Answers:** (1) flat β (univariate β column ≈ 0); size−/BM+ premia
(univariate + joint columns with large t's); absorption (rivals' slopes
die when size/BM enter the joint column). (2) When correlated regressors
share a regression, the independent-information content divides among
them per day-9's ellipse — slopes die for correlated-with-others
characteristics even when their univariate premium is real. (3) (a)
sample-period specificity — β is priced in earlier/other samples;
(b) errors-in-variables in estimated β attenuating its slope — answered
*partially* by portfolio-level pre-ranking: grouping shrinks the
estimation error variance of the assigned betas before the FM stage
(your E3 measures by how much).
