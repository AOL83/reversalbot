from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class HeartbeatMonitor:
    max_lag_s: int
    last_beat: datetime | None = None

    def beat(self, timestamp: datetime) -> None:
        self.last_beat = timestamp

    def is_stale(self, now: datetime) -> bool:
        if self.last_beat is None:
            return True
        return now - self.last_beat > timedelta(seconds=self.max_lag_s)
