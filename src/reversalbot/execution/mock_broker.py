from __future__ import annotations

import itertools
from dataclasses import dataclass

from reversalbot.execution.interfaces import Broker, OrderRequest, OrderResult


@dataclass
class MockBroker(Broker):
    def __post_init__(self) -> None:
        self._counter = itertools.count(1)
        self._orders: dict[str, OrderRequest] = {}

    def place_order(self, request: OrderRequest) -> OrderResult:
        order_id = f"mock-{next(self._counter)}"
        self._orders[order_id] = request
        return OrderResult(order_id=order_id, status="accepted")

    def cancel_all(self) -> int:
        count = len(self._orders)
        self._orders.clear()
        return count
