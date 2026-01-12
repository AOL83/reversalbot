from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class HealthStatus:
    status: str
    checked_at: datetime


def check_health() -> HealthStatus:
    return HealthStatus(status="ok", checked_at=datetime.now(UTC))
