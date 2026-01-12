# Configuration

Configuration files are YAML. Defaults can be overridden via environment variables.

## Environment Overrides
- Use the prefix `REVERSALBOT__`.
- Nested keys are separated by double underscores.
- Values are parsed as bool, int, or float when possible.

Example:
```
REVERSALBOT__RISK__MAX_DRAWDOWN_PCT=8.5
REVERSALBOT__LOGGING__LEVEL=DEBUG
```
