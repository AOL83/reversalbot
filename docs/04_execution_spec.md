# Execution Spec (Stage 1)

## Order lifecycle
1. Create order with idempotency key and stop intent.
2. Router validates kill/pause state and risk checks.
3. Broker acknowledges order and returns fills.
4. Router records fill and updates positions.

## Idempotency
- Every order must include a unique idempotency key.
- Router caches processed keys and rejects duplicates.

## Cancel/replace
Stage 1 uses mocks only. Stage 2+ will implement cancel/replace with order state
tracking.

## Flatten behavior
- Flatten closes **all positions** immediately in mock broker.
- Flatten is used by manual controls and kill switch workflows.
