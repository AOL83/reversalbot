from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass(frozen=True)
class OrderRequest:
    symbol: str
    side: OrderSide
    quantity: float


@dataclass(frozen=True)
class OrderResult:
    order_id: str
    status: str


class Broker(Protocol):
    def place_order(self, request: OrderRequest) -> OrderResult: ...

    def cancel_all(self) -> int: ...
