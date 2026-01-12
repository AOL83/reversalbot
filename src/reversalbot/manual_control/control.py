from __future__ import annotations

from dataclasses import dataclass

from reversalbot.execution.interfaces import Broker
from reversalbot.risk.kill_switch import KillSwitch


@dataclass
class ManualController:
    broker: Broker
    kill_switch: KillSwitch
    paused: bool = False

    def pause(self) -> None:
        self.paused = True

    def resume(self) -> None:
        if not self.kill_switch.engaged:
            self.paused = False

    def flatten(self) -> int:
        return self.broker.cancel_all()

    def kill(self, reason: str) -> None:
        self.kill_switch.engage(reason)
        self.paused = True

    def reset_kill(self) -> None:
        self.kill_switch.reset()
