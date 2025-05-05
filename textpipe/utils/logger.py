"""Configured logger with proper handlers."""

import logging
from textpipe.config.config import Config

logger = logging.getLogger("textpipe")
logger.setLevel(Config.get().logging["level"])

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
