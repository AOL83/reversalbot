# Failure Modes

Stage 1 enumerates failure scenarios to ensure the scaffold is resilient before
moving on.

## Common failure modes

- Missing or malformed configuration.
- Anomalous market data spikes.
- Exceeded exposure or drawdown limits.
- Duplicate order submissions.
- Repeated broker execution failures.

## Mitigations

- Strict configuration validation.
- Anomaly detection for price/volume changes.
- Idempotent order routing.
- Kill switch activation after repeated errors.
