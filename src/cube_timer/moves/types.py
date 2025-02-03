from enum import Enum, StrEnum, auto


class MoveType(Enum):
    NORMAL = auto
    PRIME = auto
    DOUBLE = auto


class Direction(StrEnum):
    RIGHT = "R"
    LEFT = "L"
    FRONT = "F"
    BACK = "B"
    UP = "U"
    DOWN = "D"
