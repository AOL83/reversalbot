"""Execution interfaces and data models."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from reversalbot.risk.stop_manager import StopIntent


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass(frozen=True)
class Order:
    order_id: str
    symbol: str
    side: OrderSide
    quantity: float
    price: float
    stop_intent: StopIntent
    idempotency_key: str


@dataclass(frozen=True)
class Fill:
    order_id: str
    symbol: str
    side: OrderSide
    quantity: float
    price: float
    slippage_bps: float


@dataclass(frozen=True)
class Position:
    symbol: str
    quantity: float
    average_price: float


class Broker(Protocol):
    def place_order(self, order: Order) -> Fill: ...

    def cancel_order(self, order_id: str) -> None: ...

    def get_positions(self) -> list[Position]: ...

    def flatten(self) -> list[Fill]: ...
