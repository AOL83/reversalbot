from __future__ import annotations

from enum import Enum


class KillSwitchState(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    KILLED = "killed"


class KillSwitch:
    def __init__(self) -> None:
        self._state: KillSwitchState = KillSwitchState.ACTIVE

    @property
    def state(self) -> KillSwitchState:
        return self._state

    @property
    def is_active(self) -> bool:
        return self._state == KillSwitchState.ACTIVE

    @property
    def is_paused(self) -> bool:
        return self._state == KillSwitchState.PAUSED

    @property
    def is_killed(self) -> bool:
        return self._state == KillSwitchState.KILLED

    def pause(self) -> None:
        if self._state != KillSwitchState.KILLED:
            self._state = KillSwitchState.PAUSED

    def resume(self) -> None:
        if self._state != KillSwitchState.KILLED:
            self._state = KillSwitchState.ACTIVE

    def kill(self) -> None:
        self._state = KillSwitchState.KILLED

    def reset(self) -> None:
        self._state = KillSwitchState.ACTIVE
