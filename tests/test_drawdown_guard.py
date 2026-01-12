from __future__ import annotations

from reversalbot.risk.drawdown_guard import DrawdownGuard


def test_drawdown_guard_breach() -> None:
    guard = DrawdownGuard(max_drawdown_pct=0.1, peak_equity=1000)
    guard.update(950)
    assert guard.breached is False
    guard.update(890)
    assert guard.breached is True
