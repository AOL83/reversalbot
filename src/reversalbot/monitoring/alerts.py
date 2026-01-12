from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol


@dataclass(frozen=True)
class Alert:
    message: str
    severity: str
    run_id: str
    created_at: datetime


class AlertSink(Protocol):
    def send(self, alert: Alert) -> None: ...


def build_alert(message: str, severity: str, run_id: str) -> Alert:
    return Alert(message=message, severity=severity, run_id=run_id, created_at=datetime.now(UTC))
