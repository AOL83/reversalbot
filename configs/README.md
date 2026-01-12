# Configuration

ReversalBot uses a YAML config file with strict schema validation.
Unknown keys are rejected.

## Environment overrides
Use the format:

```
REVERSALBOT__SECTION__FIELD=value
```

Example:
```
REVERSALBOT__LOGGING__LEVEL=DEBUG
REVERSALBOT__RISK__MAX_DRAWDOWN_PCT=8.5
```
