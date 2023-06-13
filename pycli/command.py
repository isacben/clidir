
from typing import Protocol

class BaseCommand(Protocol):
    def run(self, args: list[str]):
        """runs a command"""