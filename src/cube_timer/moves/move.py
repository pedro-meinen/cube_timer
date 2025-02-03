from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import override

from .types import Direction as Directions
from .types import MoveType as MoveType


@dataclass(repr=False)
class Move(metaclass=ABCMeta):
    direction: Directions
    type: MoveType

    @abstractmethod
    def should_skip(self, last_move: "Move") -> bool:
        pass

    @abstractmethod
    def should_invert(self, last_move: "Move") -> bool:
        pass

    @abstractmethod
    def should_double(self, last_move: "Move") -> bool:
        pass

    @property
    @abstractmethod
    def inverted_move(self) -> "Move":
        pass

    @property
    @abstractmethod
    def doubled_move(self) -> "Move":
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass(repr=False)
class NormalMove(Move):
    direction: Directions
    type: MoveType = MoveType.NORMAL

    @override
    def should_skip(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.PRIME:
            return True

        return False

    @override
    def should_invert(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.DOUBLE:
            return True

        return False

    @override
    def should_double(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.NORMAL:
            return True

        return False

    @property
    @override
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.direction)

    @property
    @override
    def inverted_move(self) -> "PrimeMove":
        return PrimeMove(self.direction)

    @override
    def __str__(self) -> str:
        return self.direction


@dataclass(repr=False)
class PrimeMove(Move):
    direction: Directions
    type: MoveType = MoveType.PRIME

    @override
    def should_skip(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.NORMAL:
            return True

        return False

    @override
    def should_invert(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.DOUBLE:
            return True

        return False

    @override
    def should_double(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.PRIME:
            return True

        return False

    @property
    @override
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.direction)

    @property
    @override
    def inverted_move(self) -> NormalMove:
        return NormalMove(self.direction)

    @override
    def __str__(self) -> str:
        return f"{self.direction}'"


@dataclass(repr=False)
class DoubleMove(Move):
    direction: Directions
    type: MoveType = MoveType.DOUBLE

    @override
    def should_skip(self, last_move: Move) -> bool:
        if self.direction == last_move.direction and last_move.type == MoveType.DOUBLE:
            return True

        return False

    @override
    def should_invert(self, last_move: Move) -> bool:
        self._last = last_move.type

        match last_move.type:
            case MoveType.NORMAL:
                return True if self.direction == last_move.direction else False
            case MoveType.PRIME:
                return True if self.direction == last_move.direction else False
            case MoveType.DOUBLE:
                return False

    @override
    def should_double(self, last_move: Move) -> bool:
        return False

    @property
    @override
    def doubled_move(self) -> "DoubleMove":
        return DoubleMove(self.direction)

    @property
    @override
    def inverted_move(self) -> Move:
        match self._last:
            case MoveType.NORMAL:
                return PrimeMove(self.direction)
            case MoveType.PRIME:
                return NormalMove(self.direction)
            case MoveType.DOUBLE:
                return DoubleMove(self.direction)

    @override
    def __str__(self) -> str:
        return f"{self.direction}2"
