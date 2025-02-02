from dataclasses import dataclass
from typing import override

from .move import Move
from .normal import NormalMove


@dataclass
class PrimeMove(Move):
    direction: str
    type: str = "Prime"

    @override
    def should_skip(self, last_move: Move) -> bool:
        if last_move.type == "Normal":
            return True

        return False

    @override
    def should_invert(self, last_move: Move) -> bool:
        if last_move.type == "Double":
            return True

        return False

    @property
    @override
    def inverted_move(self) -> NormalMove:
        return NormalMove(self.direction)
