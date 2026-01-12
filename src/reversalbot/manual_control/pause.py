"""Pause and resume controls."""

from __future__ import annotations

from reversalbot.risk.kill_switch import KillSwitch


def pause(kill_switch: KillSwitch, reason: str) -> None:
    kill_switch.pause(reason)


def resume(kill_switch: KillSwitch, reason: str) -> None:
    kill_switch.resume(reason)
