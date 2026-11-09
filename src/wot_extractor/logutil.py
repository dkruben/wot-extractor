"""Configuracao de logging (consola + ficheiro opcional)."""

from __future__ import annotations

import logging
from pathlib import Path

LOGGER_NAME = "wot_extractor"


def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(LOGGER_NAME if not name else f"{LOGGER_NAME}.{name}")


def setup_logging(verbosity: int = 0, log_file: Path | None = None) -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG if verbosity >= 2 else logging.INFO if verbosity == 1 else logging.WARNING)
    console.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(console)

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        logger.addHandler(fh)
    return logger
