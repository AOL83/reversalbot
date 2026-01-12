from __future__ import annotations

from dataclasses import dataclass

from reversalbot.execution.interfaces import Broker, OrderRequest, OrderResult
from reversalbot.risk.kill_switch import KillSwitch


@dataclass
class OrderRouter:
    broker: Broker
    kill_switch: KillSwitch

    def __post_init__(self) -> None:
        self._idempotency_cache: dict[str, OrderResult] = {}

    def submit_order(self, request: OrderRequest, idempotency_key: str) -> OrderResult:
        if self.kill_switch.engaged:
            raise RuntimeError("Kill switch engaged")
        if idempotency_key in self._idempotency_cache:
            return self._idempotency_cache[idempotency_key]
        result = self.broker.place_order(request)
        self._idempotency_cache[idempotency_key] = result
        return result
