from __future__ import annotations

from pathlib import Path

import pytest

from reversalbot.config import load_config


def test_load_config_defaults(tmp_path: Path) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text("{}")

    config = load_config(config_path)

    assert config.app.environment == "dev"
    assert config.risk.max_drawdown_pct == 10.0


def test_env_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text("{}")

    monkeypatch.setenv("REVERSALBOT__RISK__MAX_DRAWDOWN_PCT", "8.5")

    config = load_config(config_path)

    assert config.risk.max_drawdown_pct == 8.5
