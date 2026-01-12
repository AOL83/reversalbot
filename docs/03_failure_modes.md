# 03 - Failure Modes

The system is designed to fail safely. Typical failure modes include:

- **Stale data feeds:** heartbeat monitor flags when inputs are too old.
- **Execution drift:** idempotent order routing prevents duplicate fills.
- **Runaway exposure:** drawdown guard and exposure limits halt trading.
- **Infrastructure issues:** kill switch allows manual shutdown.

Each failure mode must have a documented detection and response path.
