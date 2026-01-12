"""Kill switch state machine."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class KillState(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    KILLED = "killed"


@dataclass
class KillSwitch:
    state: KillState = KillState.ACTIVE
    reasons: list[str] = field(default_factory=list)

    def pause(self, reason: str) -> None:
        if self.state is KillState.KILLED:
            return
        self.state = KillState.PAUSED
        self.reasons.append(reason)

    def resume(self, reason: str) -> None:
        if self.state is KillState.KILLED:
            return
        self.state = KillState.ACTIVE
        self.reasons.append(reason)

    def kill(self, reason: str) -> None:
        self.state = KillState.KILLED
        self.reasons.append(reason)

    def reset(self, reason: str) -> None:
        self.state = KillState.ACTIVE
        self.reasons.append(reason)

    def is_active(self) -> bool:
        return self.state is KillState.ACTIVE

    def is_paused(self) -> bool:
        return self.state is KillState.PAUSED

    def is_killed(self) -> bool:
        return self.state is KillState.KILLED
