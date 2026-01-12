# Failure Modes (Stage 1 Awareness)

Documented to prevent silent regressions and remind contributors of realistic
execution hazards.

## Execution hazards
- Slippage spikes
- Spread widening
- Wicks and price gaps
- Partial fills
- Cancel/replace lag
- API throttling and disconnects
- Retry storms causing duplicate orders

## System hazards
- Stale configs or env overrides
- Missing idempotency keys
- Loss of monitoring/alert pipeline
- State drift between router and broker

Stage 1 uses mocks to surface these issues in a controlled environment.
