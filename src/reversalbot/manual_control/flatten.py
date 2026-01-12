from __future__ import annotations

from reversalbot.execution.interfaces import Broker


def flatten(broker: Broker) -> None:
    broker.flatten()
