from dataclasses import dataclass
from typing import override

from .move import Move


@dataclass
class DoubleMove(Move):
    direction: str
    type = "Double"

    @override
    def should_skip(self, last_move: Move) -> bool:
        if last_move.type == "Double":
            return True

        return False
