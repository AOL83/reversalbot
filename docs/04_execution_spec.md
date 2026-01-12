# Execution Specification

Stage 1 execution is mock-only. Orders are not transmitted to any live venue.

## Order flow

1. Receive intent from the strategy module.
2. Validate against risk controls.
3. Apply idempotency checks to avoid duplicate execution.
4. Record the decision in logs/state.

## Idempotency

Orders must include an idempotency key. The router will reject duplicates and
return the prior decision.
