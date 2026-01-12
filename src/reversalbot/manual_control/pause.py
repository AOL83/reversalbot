from __future__ import annotations

from reversalbot.risk.kill_switch import KillSwitch


def pause(kill_switch: KillSwitch) -> None:
    kill_switch.pause()


def resume(kill_switch: KillSwitch) -> None:
    kill_switch.resume()
