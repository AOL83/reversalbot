"""Order routing with idempotency and kill switch enforcement."""

from __future__ import annotations

from dataclasses import dataclass, field

from reversalbot.errors import KillSwitchEngagedError, PauseEngagedError
from reversalbot.execution.interfaces import Broker, Fill, Order
from reversalbot.risk.kill_switch import KillSwitch


@dataclass
class OrderRouter:
    broker: Broker
    kill_switch: KillSwitch
    processed: dict[str, Fill] = field(default_factory=dict)

    def send_order(self, order: Order) -> Fill:
        if self.kill_switch.is_killed():
            raise KillSwitchEngagedError("Kill switch engaged; order rejected.")
        if self.kill_switch.is_paused():
            raise PauseEngagedError("Pause engaged; order rejected.")
        if order.idempotency_key in self.processed:
            return self.processed[order.idempotency_key]
        fill = self.broker.place_order(order)
        self.processed[order.idempotency_key] = fill
        return fill
