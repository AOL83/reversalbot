from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Symbol:
    value: str


@dataclass(frozen=True)
class Market:
    base: str
    quote: str


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"


class ReasonCode(str, Enum):
    USER = "user"
    RISK = "risk"
    SYSTEM = "system"
