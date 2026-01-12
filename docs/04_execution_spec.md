# 04 - Execution Spec

Execution is built around a broker interface that supports idempotent order routing.

## Requirements
- Orders must include an idempotency key.
- All executions must respect the kill switch.
- The mock broker is the default implementation.

## Idempotency
If the same idempotency key is submitted multiple times, the router returns the
original order result instead of placing a new order.
