from __future__ import annotations

import logging
from typing import Any, MutableMapping

from reversalbot.config import LoggingConfig


class RunLoggerAdapter(logging.LoggerAdapter[logging.Logger]):
    def process(
        self, msg: str, kwargs: MutableMapping[str, Any]
    ) -> tuple[str, MutableMapping[str, Any]]:
        extra = kwargs.setdefault("extra", {})
        if isinstance(extra, dict):
            extra["run_id"] = self.extra.get("run_id") if self.extra else None
        return msg, kwargs


def configure_logging(config: LoggingConfig, run_id: str) -> RunLoggerAdapter:
    logging.basicConfig(level=config.level)
    logger = logging.getLogger("reversalbot")
    return RunLoggerAdapter(logger, {"run_id": run_id})
