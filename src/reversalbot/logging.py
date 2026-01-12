"""Structured logging helpers."""

from __future__ import annotations

import logging
import uuid
from typing import Any


class RunLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict[str, Any]) -> tuple[str, dict[str, Any]]:
        extra = kwargs.get("extra", {})
        extra["run_id"] = self.extra.get("run_id", "")
        kwargs["extra"] = extra
        return msg, kwargs


def configure_logging(level: str) -> tuple[RunLoggerAdapter, str]:
    run_id = uuid.uuid4().hex
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s run_id=%(run_id)s %(message)s",
    )
    logger = logging.getLogger("reversalbot")
    return RunLoggerAdapter(logger, {"run_id": run_id}), run_id


def get_logger(name: str, run_id: str) -> RunLoggerAdapter:
    logger = logging.getLogger(name)
    return RunLoggerAdapter(logger, {"run_id": run_id})
