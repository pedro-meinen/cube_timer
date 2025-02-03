from dataclasses import dataclass
from typing import Protocol

from .types import Direction as Direction
from .types import Face as Face


@dataclass(repr=False)
class Move(Protocol):
    face: Face
    direction: Direction

    def __str__(self) -> str: ...

    def should_skip(self, last_move: "Move") -> bool: ...

    def should_invert(self, last_move: "Move") -> bool: ...

    def should_double(self, last_move: "Move") -> bool: ...

    @property
    def inverted_move(self) -> "Move": ...

    @property
    def doubled_move(self) -> "Move": ...


@dataclass(repr=False)
class NormalMove:
    face: Face
    direction: Direction = Direction.NORMAL

    def should_skip(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.PRIME:
            return True

        return False

    def should_invert(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.DOUBLE:
            return True

        return False

    def should_double(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.NORMAL:
            return True

        return False

    @property
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.face)

    @property
    def inverted_move(self) -> "PrimeMove":
        return PrimeMove(self.face)

    def __str__(self) -> str:
        return self.face


@dataclass(repr=False)
class PrimeMove(Move):
    face: Face
    direction: Direction = Direction.PRIME

    def should_skip(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.NORMAL:
            return True

        return False

    def should_invert(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.DOUBLE:
            return True

        return False

    def should_double(self, last_move: Move) -> bool:
        if self.face == last_move.face and last_move.direction == Direction.PRIME:
            return True

        return False

    @property
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.face)

    @property
    def inverted_move(self) -> NormalMove:
        return NormalMove(self.face)

    def __str__(self) -> str:
        return f"{self.face}'"


@dataclass(repr=False)
class DoubleMove(Move):
    face: Face
    direction: Direction = Direction.DOUBLE

    def should_skip(self, last_move: Move) -> bool:
        if (
            self.direction == last_move.direction
            and last_move.direction == Direction.DOUBLE
        ):
            return True

        return False

    def should_invert(self, last_move: Move) -> bool:
        self._last = last_move.direction

        match last_move.direction:
            case Direction.NORMAL:
                return True if self.face == last_move.face else False
            case Direction.PRIME:
                return True if self.face == last_move.face else False
            case Direction.DOUBLE:
                return False

    def should_double(self, last_move: Move) -> bool:
        return False

    @property
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.face)

    @property
    def inverted_move(self) -> Move:
        match self._last:
            case Direction.NORMAL:
                return PrimeMove(self.face)
            case Direction.PRIME:
                return NormalMove(self.face)
            case Direction.DOUBLE:
                return DoubleMove(self.face)

    def __str__(self) -> str:
        return f"{self.face}2"
