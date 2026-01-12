"""Application configuration using Pydantic models."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import os

import yaml
from pydantic import BaseModel, ConfigDict, Field


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = "ReversalBot"
    environment: str = "local"
    run_id: str = ""


class LoggingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: str = "INFO"


class RiskConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    risk_per_trade: float = Field(ge=0.0, le=1.0)
    max_notional_per_symbol: float = Field(gt=0.0)
    max_total_notional: float = Field(gt=0.0)
    max_drawdown_pct: float = Field(ge=0.0, le=1.0)


class BrokerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    base_currency: str = "USD"
    default_slippage_bps: int = Field(ge=0)
    default_spread_bps: int = Field(ge=0)


class AnomalyConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_spread_bps: int = Field(ge=0)
    max_slippage_bps: int = Field(ge=0)
    max_error_rate: float = Field(ge=0.0, le=1.0)


class ReversalBotConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    app: AppConfig = AppConfig()
    logging: LoggingConfig = LoggingConfig()
    risk: RiskConfig
    broker: BrokerConfig
    anomaly: AnomalyConfig


def _load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        msg = "Config file must contain a mapping."
        raise ValueError(msg)
    return data


def _apply_env_overrides(base: dict[str, Any]) -> dict[str, Any]:
    overrides: dict[str, Any] = {}
    prefix = "REVERSALBOT__"
    for key, value in os.environ.items():
        if not key.startswith(prefix):
            continue
        parts = key[len(prefix) :].lower().split("__")
        current: dict[str, Any] = overrides
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value

    def merge(target: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
        for k, v in source.items():
            if isinstance(v, dict) and isinstance(target.get(k), dict):
                target[k] = merge(target[k], v)
            else:
                target[k] = v
        return target

    return merge(base, overrides)


def load_config(path: str | Path) -> ReversalBotConfig:
    config_path = Path(path)
    raw = _load_yaml(config_path)
    merged = _apply_env_overrides(raw)
    return ReversalBotConfig.model_validate(merged)
