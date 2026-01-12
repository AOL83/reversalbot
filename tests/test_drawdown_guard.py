from __future__ import annotations

from reversalbot.risk.drawdown_guard import DrawdownGuard


def test_drawdown_guard_triggers() -> None:
    guard = DrawdownGuard(max_drawdown_pct=10.0, peak_equity=1000.0)

    triggered = guard.update_equity(850.0)

    assert triggered is True
    assert guard.current_drawdown_pct == 15.0
