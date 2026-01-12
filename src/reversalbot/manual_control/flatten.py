"""Flatten all positions."""

from __future__ import annotations

from reversalbot.execution.interfaces import Broker, Fill


def flatten_all(broker: Broker) -> list[Fill]:
    return broker.flatten()
