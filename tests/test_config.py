from __future__ import annotations

from pathlib import Path

import pytest

from reversalbot.config import load_config


def test_load_config_with_env_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        """
app:
  name: "ReversalBot"
  environment: "local"
  run_id: ""
logging:
  level: "INFO"
risk:
  risk_per_trade: 0.01
  max_notional_per_symbol: 1000
  max_total_notional: 5000
  max_drawdown_pct: 0.1
broker:
  base_currency: "USD"
  default_slippage_bps: 5
  default_spread_bps: 2
anomaly:
  max_spread_bps: 10
  max_slippage_bps: 15
  max_error_rate: 0.05
"""
    )
    monkeypatch.setenv("REVERSALBOT__RISK__MAX_TOTAL_NOTIONAL", "8000")
    config = load_config(config_path)
    assert config.risk.max_total_notional == 8000
