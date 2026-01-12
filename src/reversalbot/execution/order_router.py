from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderRequest:
    idempotency_key: str
    symbol: str
    side: str
    quantity: float
    price: float


@dataclass(frozen=True)
class OrderResult:
    status: str
    message: str


class IdempotentOrderRouter:
    def __init__(self) -> None:
        self._seen: dict[str, OrderResult] = {}

    def route(self, order: OrderRequest) -> OrderResult:
        if order.idempotency_key in self._seen:
            return self._seen[order.idempotency_key]
        result = OrderResult(status="accepted", message="mock order accepted")
        self._seen[order.idempotency_key] = result
        return result
