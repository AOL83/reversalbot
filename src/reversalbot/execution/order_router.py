from __future__ import annotations

from reversalbot.errors import KillSwitchEngagedError, RouterPausedError
from reversalbot.execution.interfaces import Broker, Fill, Order
from reversalbot.risk.kill_switch import KillSwitch


class IdempotentOrderRouter:
    def __init__(self, broker: Broker, kill_switch: KillSwitch) -> None:
        self._broker = broker
        self._kill_switch = kill_switch
        self._fills: dict[str, Fill] = {}

    def route(self, order: Order, idempotency_key: str) -> Fill:
        if idempotency_key in self._fills:
            return self._fills[idempotency_key]
        if self._kill_switch.is_killed:
            raise KillSwitchEngagedError("Kill switch engaged")
        if self._kill_switch.is_paused:
            raise RouterPausedError("Routing paused")
        if order.stop_intent is not None:
            order.stop_intent.validate()
        fill = self._broker.submit_order(order)
        self._fills[idempotency_key] = fill
        return fill
