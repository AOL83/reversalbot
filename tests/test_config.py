from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from reversalbot.config import load_config


def write_config(tmp_path: Path, payload: str) -> Path:
    path = tmp_path / "config.yaml"
    path.write_text(payload, encoding="utf-8")
    return path


def test_config_loads(tmp_path: Path) -> None:
    path = write_config(
        tmp_path,
        """
app:
  name: reversalbot
  environment: test
  run_id: run-123
logging:
  level: INFO
risk:
  risk_per_trade: 0.02
  max_notional_per_symbol: 1000.0
  max_total_notional: 3000.0
  max_drawdown_pct: 5.0
broker:
  base_currency: USD
  default_slippage_bps: 1.0
  default_spread_bps: 1.0
anomaly:
  max_spread_bps: 5.0
  max_slippage_bps: 6.0
  max_error_rate: 0.02
""",
    )
    config = load_config(path)
    assert config.app.run_id == "run-123"


def test_config_forbids_unknown_keys(tmp_path: Path) -> None:
    path = write_config(
        tmp_path,
        """
app:
  name: reversalbot
  environment: test
  run_id: run-123
  unknown_key: nope
logging:
  level: INFO
risk:
  risk_per_trade: 0.02
  max_notional_per_symbol: 1000.0
  max_total_notional: 3000.0
  max_drawdown_pct: 5.0
broker:
  base_currency: USD
  default_slippage_bps: 1.0
  default_spread_bps: 1.0
anomaly:
  max_spread_bps: 5.0
  max_slippage_bps: 6.0
  max_error_rate: 0.02
""",
    )
    with pytest.raises(ValidationError):
        load_config(path)
