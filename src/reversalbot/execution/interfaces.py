from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol

from reversalbot.domain.models import Side, Symbol
from reversalbot.risk.stop_manager import StopIntent


@dataclass(frozen=True)
class Order:
    order_id: str
    symbol: Symbol
    side: Side
    quantity: float
    price: float
    stop_intent: StopIntent | None = None


@dataclass(frozen=True)
class Fill:
    order_id: str
    symbol: Symbol
    side: Side
    quantity: float
    price: float
    executed_at: datetime


@dataclass
class Position:
    symbol: Symbol
    quantity: float
    average_price: float


class Broker(Protocol):
    def submit_order(self, order: Order) -> Fill: ...

    def positions(self) -> list[Position]: ...

    def flatten(self) -> None: ...


def build_fill(order: Order) -> Fill:
    return Fill(
        order_id=order.order_id,
        symbol=order.symbol,
        side=order.side,
        quantity=order.quantity,
        price=order.price,
        executed_at=datetime.now(UTC),
    )
