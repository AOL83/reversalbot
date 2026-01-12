from __future__ import annotations

from reversalbot.risk.kill_switch import KillState, KillSwitch


def test_kill_switch_transitions() -> None:
    kill_switch = KillSwitch()
    assert kill_switch.state is KillState.ACTIVE

    kill_switch.pause("maintenance")
    assert kill_switch.state is KillState.PAUSED

    kill_switch.resume("resume")
    assert kill_switch.state is KillState.ACTIVE

    kill_switch.kill("risk breach")
    assert kill_switch.state is KillState.KILLED
