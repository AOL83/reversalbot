# Configuration

## Precedence
1. CLI `--config` YAML file.
2. Environment variable overrides.

## Environment overrides
Use `REVERSALBOT__SECTION__FIELD` format.

Example:
```bash
export REVERSALBOT__RISK__MAX_TOTAL_NOTIONAL=50000
```

Values are parsed by Pydantic based on field type.
