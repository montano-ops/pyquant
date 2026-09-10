# Review — Random Experiments & Events

## Retrieval

1. Experiment / sample space / event — with trading examples.
2. What is "one realization" and why does it matter for backtests?
3. Why must events be precise sets rather than vibes?

<details><summary>Answers</summary>

1. Experiment: tomorrow's return process. Ω: all possible returns. Event:
   any subset, e.g. {r > 1%}.
2. Data = one path from a random process; statistics summarize that path,
   not the truth — lucky paths look like skill (orientation day 5).
3. Imprecise events can't be measured; measurement requires a set you can
   filter for in code.

</details>

## Elaboration

- Convert "this strategy blows up occasionally" into a measurable event,
  and say what data you'd need to estimate its probability.

## Spaced repetition

- Revisit with day 4 (random variables) — the event language becomes the
  distribution language.
