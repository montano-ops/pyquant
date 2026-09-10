# Review — Module 02 Checkpoint

## Self-assessment against the rubric

- [ ] Exact binomial computed (not just the approximation)
- [ ] p-value interpreted correctly (P(data this extreme | H₀), never
      P(H₀ | data))
- [ ] Simulation agrees with exact to MC error
- [ ] Power computed and *interpreted* (what a skilled trader still
      endures)
- [ ] n_eff direction argued correctly
- [ ] Memo's final sentence is quotable and correct

<details><summary>The quotable sentence (compare yours)</summary>

"A 55% observed win rate over one year is consistent with anything from a
fair coin flip having a good year to a genuinely modest edge, and does not
by itself establish skill — only multiple years of data, pre-committed
evaluation rules, and cost-aware expectancy can begin to do that."

The precise p-value (exact binomial ≈ 7% one-sided under the coin flip;
normal ≈ 6.5%) makes it *mildly* interesting but far from conclusive;
the power computation (a true 53% trader shows ≥55% in a year only ~30%
of the time, and still has a sub-50% year about one year in six) shows
the year is nearly as compatible with modest skill as with none. n_eff < 252 under regime
dependence widens everything further.

</details>

## The module in one paragraph (write it, then compare)

Probability gave you: the event language (1–3), the distribution language
(4–5), dependence and its price (8–9), the counting machinery of win rates
(10), the two theorems that make statistics possible (12, 15), and the
simulation habit that replaces "what happened" with "what could have
happened" (17–19). Module 03 now points this machinery at real return
distributions — and finds them heavier-tailed and less stable than the
toys. That's not a problem for the toolkit; that's why the toolkit exists.
