# Day 18 — Review: Which SE When

**Time budget:** ~15 min the next morning; ~5 min on weekly review.

## The 90-second version

A standard error is a **claim about the residual process** — and claims
are checked by tournaments, not trust. Four planted worlds, one matrix:
the classical sandwich certifies exactly one world (iid); White repairs
the variance-fan and exactly nothing else; Newey–West repairs
overlap-induced memory (given L ≥ horizon — and only asymptotically:
~11–14% residual rejection at strong overlap, which is why the
non-overlapped re-estimate is the exact repair); Fama–MacBeth alone
survives the panel row. Every estimate carries its flavor; every flavor
is licensed by a mechanism; every mechanism has a diagnostic that names
it before you fit anything.

## Retrieval practice (close everything first)

1. Complete the sentence and know why it's the whole day: "choosing the
   SE flavor means choosing ___."
2. The four-world matrix: name each world's identifying signature you
   diagnose BEFORE fitting, and the estimator that survived its row.
3. Two false comforts, with their tournament numbers.
4. Recite the flowchart's four leaves from the E4 drill.

*(Answers: (1) "...the failure mode of your residuals you are willing to
be wrong about." (2) iid: nothing — classical (~4–5%); het: variance
traces |x| — White (classical ~23% → ~4–5%); overlap: the ramp ACF of
rolling sums — NW at L ≥ 21 (classical/White ~60–65%, NW(3) only down
to ~28%, NW(21) ~11–14% residual = consistent-not-exact); panel:
cross-sectional dependence within month on persistent characteristics
— FM (pooled-anything ~35–40%, FM ~4%). (3) White-on-overlap (~63%
rejection — diagonal meat, memoryless world); NW(3)-on-a-21-day-overlap
(~28% — a partial repair is still a failure). (4) Panel? → FM + λ̂_t ACF
check → overlapping horizon h? → NW with L ≥ h (or drop the overlap) →
variance traces |x|? → White → else classical, and show the residuals
prove it.)*

## If you had to re-derive one thing

The **overlap effective-n arithmetic**: 3000 overlapped 21-day "months"
contain ≈ 3000/21 ≈ 143 independent pieces of information — which is why
classical t's there inflate by ~√21, why the tournament row shows ~60%
false positives, and why every long-horizon regression's power analysis
starts from effective n, not calendar n. Write the three steps cold.

## Bookmark for module 06.19 (and 07+)

This day is the certification engine of the module's research protocol:
day 19's study and every asset-pricing regression you will ever read is
an entry in one of these four rows (usually two at once: panels ARE the
default habitat; moment conditions in module 09 generalize the whole
framework). The habit to keep: before any t-stat leaves your notebook,
name the world you're assuming and the one diagnostic that says you're
allowed.
