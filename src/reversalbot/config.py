from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, cast

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = "reversalbot"
    environment: str = "dev"
    dry_run: bool = True
    data_dir: Path = Path("./data")


class LoggingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: str = "INFO"
    json: bool = False

    @field_validator("level")
    @classmethod
    def normalize_level(cls, value: str) -> str:
        normalized = value.strip().upper()
        if normalized not in logging.getLevelNamesMapping():
            msg = f"Unknown logging level: {value}"
            raise ValueError(msg)
        return normalized


class RiskConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_drawdown_pct: float = Field(default=10.0, gt=0)
    max_notional_per_symbol: float = Field(default=25000.0, gt=0)
    max_total_notional: float = Field(default=100000.0, gt=0)
    max_trades_per_day: int = Field(default=20, gt=0)
    kill_switch_enabled: bool = True


class BrokerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = "mock-broker"
    api_base_url: str = "https://broker.example.com"
    account_id: str = "demo-account"


class AnomalyConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    max_price_change_pct: float = Field(default=5.0, gt=0)
    max_volume_spike: float = Field(default=3.0, gt=0)


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
        data = _parse_simple_yaml(handle.read())
    return data


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, root)]

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        while indent < stack[-1][0]:
            stack.pop()
        current = stack[-1][1]
        key, separator, remainder = stripped.partition(":")
        if separator == "":
            msg = f"Invalid config line: {line}"
            raise ValueError(msg)
        key = key.strip()
        value = remainder.strip()
        if value == "":
            child: dict[str, Any] = {}
            current[key] = child
            stack.append((indent + 2, child))
        else:
            current[key] = _parse_scalar(value)

    return root


def _parse_scalar(value: str) -> Any:
    lower = value.lower()
    if lower in {"true", "false"}:
        return lower == "true"
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        return value[1:-1]
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


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
