"""Drawdown tracking and guard."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DrawdownGuard:
    max_drawdown_pct: float
    peak_equity: float
    breached: bool = False

    def update(self, equity: float) -> None:
        if equity > self.peak_equity:
            self.peak_equity = equity
        drawdown = (self.peak_equity - equity) / self.peak_equity
        if drawdown >= self.max_drawdown_pct:
            self.breached = True
