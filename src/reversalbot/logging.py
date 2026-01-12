from __future__ import annotations

import logging

from reversalbot.config import LoggingConfig


def configure_logging(config: LoggingConfig) -> None:
    mapping = logging.getLevelNamesMapping()
    logging.getLogger().setLevel(mapping[config.level])


def build_logger(name: str, config: LoggingConfig) -> logging.Logger:
    configure_logging(config)
    return logging.getLogger(name)
