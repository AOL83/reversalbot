"""Emergency stop sequence."""

from __future__ import annotations

from reversalbot.execution.interfaces import Broker, Fill
from reversalbot.risk.kill_switch import KillSwitch


def emergency_stop(kill_switch: KillSwitch, broker: Broker, reason: str) -> list[Fill]:
    kill_switch.kill(reason)
    return broker.flatten()
