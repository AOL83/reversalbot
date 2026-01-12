from __future__ import annotations

import os
from pathlib import Path
from typing import Any, cast

import yaml
from pydantic import BaseModel, ConfigDict, Field


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = "reversalbot"
    environment: str = "dev"
    run_id: str = "local-run"


class LoggingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: str = "INFO"


class RiskConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    risk_per_trade: float = Field(default=0.01, gt=0, lt=1)
    max_notional_per_symbol: float = Field(default=25000.0, gt=0)
    max_total_notional: float = Field(default=100000.0, gt=0)
    max_drawdown_pct: float = Field(default=10.0, gt=0)


class BrokerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_currency: str = "USD"
    default_slippage_bps: float = Field(default=2.0, ge=0)
    default_spread_bps: float = Field(default=1.5, ge=0)


class AnomalyConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_spread_bps: float = Field(default=5.0, gt=0)
    max_slippage_bps: float = Field(default=6.0, gt=0)
    max_error_rate: float = Field(default=0.02, ge=0)


class ReversalBotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    app: AppConfig = AppConfig()
    logging: LoggingConfig = LoggingConfig()
    risk: RiskConfig = RiskConfig()
    broker: BrokerConfig = BrokerConfig()
    anomaly: AnomalyConfig = AnomalyConfig()


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        msg = f"Config file not found: {path}"
        raise FileNotFoundError(msg)
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        msg = "Config root must be a mapping"
        raise ValueError(msg)
    return data


def _apply_env_overrides(data: dict[str, Any]) -> dict[str, Any]:
    updated = dict(data)
    prefix = "REVERSALBOT__"
    for key, value in os.environ.items():
        if not key.startswith(prefix):
            continue
        path = key[len(prefix) :].lower().split("__")
        current: dict[str, Any] = updated
        for segment in path[:-1]:
            next_node = current.get(segment)
            if not isinstance(next_node, dict):
                next_node = {}
                current[segment] = next_node
            current = next_node
        current[path[-1]] = value
    return updated


def load_config(path: Path) -> ReversalBotConfig:
    data = _load_yaml(path)
    data = _apply_env_overrides(data)
    return cast(ReversalBotConfig, ReversalBotConfig.model_validate(data))
