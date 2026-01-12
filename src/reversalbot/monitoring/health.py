"""Basic health and heartbeat snapshot."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class HealthSnapshot:
    timestamp: datetime
    status: str
    message: str


def heartbeat(status: str = "ok", message: str = "") -> HealthSnapshot:
    return HealthSnapshot(timestamp=datetime.now(timezone.utc), status=status, message=message)
