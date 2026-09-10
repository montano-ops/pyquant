# Day 21 — Module Checkpoint: Is a 55% Win Rate Luck?

## The problem (standalone — solve before opening the solution)

A trading account shows **138 winning days out of 252** (54.8%). The owner
claims skill. You will decide, with machinery you built this module, under
a series of increasingly honest assumptions. Write your analysis as if for
a client: every claim numbered, every number justified.

**Part 1 — The exact question.** Under H₀ "each day is an independent
coin flip" (p = 0.5): compute the probability of ≥138 wins in 252 days.
That's a *p-value*. State in plain words what it does and does not tell
you.

**Part 2 — The approximation.** Same computation via the normal
approximation (day 10.5/day 15): z = (p̂ − p₀)/SE. Compare with the exact
answer; explain why they differ slightly.

**Part 3 — Simulation.** Same question by Monte Carlo: simulate 100,000
years of 252 fair-coin days; report the fraction with ≥138 wins. All three
methods must agree to two significant figures.

**Part 4 — Power (the direction most people forget).** Suppose the true
win rate were 0.53 (a realistic skilled edge). What is the probability
that 252 days *shows* ≥ 138 wins? What then is the probability that a
*genuinely skilled* 0.53 trader has a sub-50% year? (Binomial CDF —
compute it.)

**Part 5 — Dependence caveat.** Days are not exactly independent (regimes).
Explain, with the n_eff formula, in which direction this shifts your
conclusion and why you cannot compute the exact correction from the win
counts alone.

**Part 6 — The verdict.** Write the client memo: what can be concluded
from 138/252, what cannot, and what evidence *would* settle the question.
End with the sentence you'd want quoted: "A 55% observed win rate over one
year is consistent with ___ and does not by itself establish ___."

**Rules:** attempt all six parts before the solution; exact → approximation
→ simulation order is mandatory (it's the module's spine); the memo is the
deliverable, not the code.

**Rubric (self-grade):** exact binomial ✓; correct p-value interpretation
(no "probability H₀ is true") ✓; simulation within MC error of exact ✓;
power computed correctly and interpreted ✓; n_eff direction correct ✓;
memo quotable ✓. Six of six = module 02 complete.
