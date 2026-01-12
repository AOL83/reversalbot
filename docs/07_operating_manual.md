# Operating Manual

Stage 1 is intended for local development and CI verification.

## Startup

1. Create a virtual environment with Poetry.
2. Copy `configs/config.example.yaml` to `configs/config.yaml` and customize if
   needed.
3. Run the CLI in dry-run mode.

## Observability

- Monitor log output for risk and anomaly alerts.
- Review test outputs in CI for regressions.
