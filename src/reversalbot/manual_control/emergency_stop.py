from __future__ import annotations

from reversalbot.risk.kill_switch import KillSwitch


def kill(kill_switch: KillSwitch) -> None:
    kill_switch.kill()


def reset_kill(kill_switch: KillSwitch) -> None:
    kill_switch.reset()
