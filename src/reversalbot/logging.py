from __future__ import annotations

import logging
from collections.abc import MutableMapping
from typing import Any, cast


class RunLoggerAdapter(logging.LoggerAdapter[logging.Logger]):
    """Logger adapter that injects run_id into structured logs."""

    def process(self, msg: str, kwargs: MutableMapping[str, Any]) -> tuple[str, Any]:
        extra = kwargs.setdefault("extra", {})
        extra_data = cast(dict[str, Any], self.extra)
        extra.setdefault("run_id", extra_data.get("run_id", "unknown"))
        return msg, kwargs


def build_logger(run_id: str, level: str) -> RunLoggerAdapter:
    logger = logging.getLogger("reversalbot")
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s run_id=%(run_id)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.propagate = False
    return RunLoggerAdapter(logger, {"run_id": run_id})
