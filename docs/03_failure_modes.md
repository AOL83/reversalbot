# Failure Modes

Expected failure modes include:
- Configuration errors or missing keys.
- Risk limit breaches.
- External system instability (Stage 2+).
- Operator mistakes.

Mitigations:
- Strict config validation with `extra = forbid`.
- Kill switch and pause/resume controls.
- Idempotent order routing to avoid double execution.
