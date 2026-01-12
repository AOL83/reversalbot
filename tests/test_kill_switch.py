from __future__ import annotations

from reversalbot.risk.kill_switch import KillSwitch


def test_kill_switch_trips_after_failures() -> None:
    switch = KillSwitch(enabled=True, max_failures=2)

    switch.record_failure("timeout")
    assert not switch.is_tripped()

    switch.record_failure("timeout")
    assert switch.is_tripped()
    assert switch.reason == "timeout"


def test_kill_switch_reset() -> None:
    switch = KillSwitch(enabled=True, max_failures=1)

    switch.record_failure("error")
    assert switch.is_tripped()

    switch.reset()
    assert not switch.is_tripped()
