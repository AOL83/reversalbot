from __future__ import annotations

from pathlib import Path

import pytest

from reversalbot.config import LoggingConfig, ReversalBotConfig, load_config


def test_load_config_defaults(tmp_path: Path) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text("app:\n  name: 'demo'\n", encoding="utf-8")

    config = load_config(config_path)

    assert config.app.name == "demo"
    assert config.risk.max_trades_per_day == 20


def test_env_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config_path = tmp_path / "config.yaml"
    config_path.write_text("app:\n  name: 'demo'\n", encoding="utf-8")

    monkeypatch.setenv("REVERSALBOT__RISK__MAX_DRAWDOWN_PCT", "8.5")

    config = load_config(config_path)

    assert config.risk.max_drawdown_pct == 8.5


def test_logging_level_normalized() -> None:
    config = ReversalBotConfig.model_validate({"logging": {"level": "info"}})

    assert config.logging.level == "INFO"


def test_logging_level_invalid() -> None:
    with pytest.raises(ValueError):
        LoggingConfig.model_validate({"level": "not-a-level"})
