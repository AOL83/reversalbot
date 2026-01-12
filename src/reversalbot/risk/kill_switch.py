from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KillSwitch:
    enabled: bool = True
    max_failures: int = 3
    failure_count: int = 0
    tripped: bool = False
    reason: str | None = None

    def record_failure(self, reason: str) -> None:
        if not self.enabled:
            return
        self.failure_count += 1
        if self.failure_count >= self.max_failures:
            self.tripped = True
            self.reason = reason

    def record_success(self) -> None:
        if not self.enabled:
            return
        self.failure_count = 0

    def reset(self) -> None:
        self.failure_count = 0
        self.tripped = False
        self.reason = None

    def is_tripped(self) -> bool:
        return self.enabled and self.tripped
