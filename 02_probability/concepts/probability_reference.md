# Probability Reference (module 02, one page)

## The vocabulary

| Term | Meaning | Trading version |
|---|---|---|
| experiment | process with uncertain outcome | a trading day |
| sample space Ω | all possible outcomes | {up day, down day} (or the whole real line for returns) |
| event | a subset of outcomes | "return > +2σ" |
| P(A) | probability of event A | long-run frequency of the event |
| P(A\|B) | probability of A *given* B | P(gain \| signal fired) |
| independence | P(A\|B) = P(A) | yesterday tells you nothing about today |
| random variable | number assigned to each outcome | the day's return |
| distribution | the full likelihood pattern | the shape of returns |

## The rules

- Complement: P(not A) = 1 − P(A)
- Union: P(A or B) = P(A) + P(B) − P(A and B)
- Conditional: P(A\|B) = P(A and B) / P(B)
- **Bayes:** P(A\|B) = P(B\|A)·P(A) / P(B) — flip the conditioning
- Independence: P(A and B) = P(A)·P(B)

## The core quantities

| Quantity | Formula | Notes |
|---|---|---|
| Expectation | E[X] = Σ p(x)·x (discrete) | long-run average; NOT a promise |
| Variance | Var(X) = E[(X − E[X])²] = E[X²] − E[X]² | squared spread |
| SD | σ = √Var | same units as X |
| Covariance | Cov(X,Y) = E[(X−E[X])(Y−E[Y])] | unnormalized co-movement |
| Correlation | ρ = Cov(X,Y)/(σ_X σ_Y) | ∈ [−1, 1]; unitless |
| Portfolio (weights w) | E = Σwᵢμᵢ; Var = ΣΣ wᵢwⱼσᵢⱼ | simple returns |

## Key theorems (intuition-first)

- **LLN**: the sample mean converges to the true mean as n grows. Converges
  at rate 1/√n — *slowly*, and slower still with fat tails.
- **CLT**: the *sample mean* (properly standardized) is approximately
  normal for large n, whatever the underlying distribution — this is why
  t-statistics work at all. Fails or slows under fat tails & dependence.

## Fallacies to be armed against

- **Gambler's fallacy**: "5 losses, so a win is due" (independence has no memory).
- **Law of small numbers**: treating small samples as if they were large
  (a 100-day track record means almost nothing when daily SNR ≈ 0.05).
- **Confusing P(A\|B) with P(B\|A)**: "most crashes had warning signal X" ≠
  "signal X mostly precedes crashes" — base rates decide.
- **Confusing correlation with causation**: ρ measures co-movement, not mechanism.
