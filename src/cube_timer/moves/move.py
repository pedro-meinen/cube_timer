from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Move(metaclass=ABCMeta):
    direction: str
    type: str

    @abstractmethod
    def should_skip(self, last_move: "Move") -> bool:
        pass

    @abstractmethod
    def should_invert(self, last_move: "Move") -> bool:
        pass

    @property
    @abstractmethod
    def inverted_move(self) -> "Move":
        pass
