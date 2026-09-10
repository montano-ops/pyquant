# Day 2 Review — Corporate Actions by Hand

## Retrieval (answers)

1. Backward cumulative factor: splits multiply the ratio (divide past
   prices), dividends multiply (1 − D/P_ex). Both apply to prices
   BEFORE the event.
2. Unit test: hand-built vs provider ratio = a constant (to ~1e−6);
   returns correlation 1.000; CRSP-convention returns identical.
3. Divergence causes: ex-date vs announcement-date timing, special
   dividends' approximation, provider rounding/floors, missed events
   (the drift).
4. Why do it once: adjusted is a construct (now you know which);
   you own an audit path; delisting returns are one more action.

## Elaboration prompts

- Your hand-built ratio drifts 0.3% over 8 years, always in jumps on
  ex-div dates. Diagnose (timing: using close BEFORE ex-date, or the
  provider using the day-after price — a one-day factor error per
  event compounds).
- Design the "action integrity" check for day 7's panel: for each
  ticker, every action date should show (a) raw-close jump ≈ ratio
  (splits), (b) adj-raw return gap ≈ D/P (dividends). Write the two
  boolean series.

## Interleaved problem

Construct: $60 stock, 3:1 reverse split, then a $2 dividend on the
post-split $70 price. What does your algorithm do to prices before
each event? What is the adjusted price of the original day-0 $60?

<details><summary>Reference answer</summary>

Reverse split 1:3: factor ÷(1/3) → past prices ×... careful: a 3:1
reverse split means 3 old shares become 1 new; price triples; past
prices are divided by 3? NO — past prices are DIVIDED by the ratio
new/old = 3: the factor for past prices is ×(1/3)? Restate cleanly:
to state past prices in new-share units, divide past raw by 3 (one
new share = 3 old). So day-0 $60 → $20 in new units... but then the
pre-event adjusted price must equal the raw price AT the event in new
units — hmm, the algorithm: adj_past = raw_past × Π(1/ratio for
splits before... ). Working answer: adjusted day-0 = 60 × (1/3)
[reverse split] × (1 − 2/70) [dividend] = 60 × 0.3333 × 0.9714 ≈
$19.43. The dividend factor applies to everything before ITS date —
including the already-split-restated past. **Reverse splits are the
classic hand-build trap: the ratio enters as its reciprocal of the
naive intuition.**
</details>

## Self-grade

- The five-line algorithm, cold?
- The reverse-split direction: derived or memorized? (Derive it once —
  "state the past in current units" — and it's yours forever.)
