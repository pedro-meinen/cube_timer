from enum import Enum, StrEnum, auto


class Direction(Enum):
    NORMAL = auto
    PRIME = auto
    DOUBLE = auto


class Face(StrEnum):
    RIGHT = "R"
    LEFT = "L"
    FRONT = "F"
    BACK = "B"
    UP = "U"
    DOWN = "D"
