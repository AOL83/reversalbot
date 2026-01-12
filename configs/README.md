# Configuration

Stage 1 uses a single YAML file to configure the ReversalBot scaffold. The example
configuration is stored in `configs/config.example.yaml`.

## Sections

- `app`: Application metadata and runtime settings.
- `logging`: Log verbosity and format.
- `risk`: Guardrails that protect capital and operational safety.
- `broker`: Mock broker connectivity details.
- `anomaly`: Detection thresholds for price/volume anomalies.

## Environment overrides

Each config value can be overridden with environment variables using the
`REVERSALBOT__` prefix. Nested keys are separated with double underscores.

Example:

```bash
export REVERSALBOT__RISK__MAX_DRAWDOWN_PCT=10
export REVERSALBOT__BROKER__ACCOUNT_ID="paper-account"
```
