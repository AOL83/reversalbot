from __future__ import annotations

from reversalbot.risk.kill_switch import KillSwitch


def test_kill_switch_engage_and_reset() -> None:
    kill_switch = KillSwitch()

    kill_switch.engage("test")
    assert kill_switch.engaged is True
    assert kill_switch.reason == "test"

    kill_switch.reset()
    assert kill_switch.engaged is False
    assert kill_switch.reason is None
