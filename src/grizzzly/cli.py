import time
from typing import Optional


class CLI:

    def __init__(self):
        self.start = time.time()

    def hello(self, name: Optional[str] = None):
        name = name or "world"
        print(f"Hello, {name}!")
