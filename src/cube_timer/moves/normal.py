from dataclasses import dataclass
from typing import override

from .move import Move
from .prime import PrimeMove


@dataclass
class NormalMove(Move):
    direction: str
    type: str = "Normal"

    @override
    def should_skip(self, last_move: Move) -> bool:
        if last_move.type == "Prime":
            return True

        return False

    @override
    def should_invert(self, last_move: Move) -> bool:
        if last_move.type == "Double":
            return True

        return False

    @property
    @override
    def inverted_move(self) -> PrimeMove:
        return PrimeMove(self.direction)
