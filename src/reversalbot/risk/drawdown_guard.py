from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DrawdownGuard:
    max_drawdown_pct: float
    peak_equity: float
    current_drawdown_pct: float = 0.0

    def update_equity(self, equity: float) -> bool:
        if equity > self.peak_equity:
            self.peak_equity = equity
        drawdown = (self.peak_equity - equity) / self.peak_equity * 100
        self.current_drawdown_pct = drawdown
        return drawdown >= self.max_drawdown_pct
