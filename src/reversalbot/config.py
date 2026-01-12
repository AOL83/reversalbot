from __future__ import annotations

import os
from pathlib import Path
from typing import Any, cast

import yaml
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    environment: str = "dev"
    run_id: str = "local"


class LoggingConfig(BaseModel):
    level: str = "INFO"
    json: bool = False


class RiskConfig(BaseModel):
    max_drawdown_pct: float = 10.0
    max_position_pct: float = 2.0
    max_notional: float = 10000.0


class BrokerConfig(BaseModel):
    name: str = "mock"
    base_currency: str = "USD"


class AnomalyConfig(BaseModel):
    max_heartbeat_lag_s: int = 60
    max_price_gap_pct: float = 5.0


class ReversalBotConfig(BaseModel):
    app: AppConfig = Field(default_factory=AppConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    risk: RiskConfig = Field(default_factory=RiskConfig)
    broker: BrokerConfig = Field(default_factory=BrokerConfig)
    anomaly: AnomalyConfig = Field(default_factory=AnomalyConfig)


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    data = yaml.safe_load(path.read_text())
    return data or {}


def _parse_value(value: str) -> Any:
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def _apply_env_overrides(data: dict[str, Any]) -> dict[str, Any]:
    result = {**data}
    prefix = "REVERSALBOT__"
    for key, value in os.environ.items():
        if not key.startswith(prefix):
            continue
        path = key[len(prefix) :].lower().split("__")
        current: dict[str, Any] = result
        for part in path[:-1]:
            current = current.setdefault(part, {})
        current[path[-1]] = _parse_value(value)
    return result


def load_config(path: Path) -> ReversalBotConfig:
    data = _load_yaml(path)
    data = _apply_env_overrides(data)
    return cast(ReversalBotConfig, ReversalBotConfig.model_validate(data))
