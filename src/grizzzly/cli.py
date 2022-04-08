import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)

class CLI:

    def __init__(self):
        self.start = time.time()

    def hello(self, name: Optional[str] = None):
        name = name or "world"
        logger.info("This is an info log!")
        logger.warning("This is a warning log!")
        logger.error("This is an error log!")
        print(f"Hello, {name}!")
