from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AlertSink:
    messages: list[str] = field(default_factory=list)

    def record(self, message: str) -> None:
        self.messages.append(message)
