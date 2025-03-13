from enum import Enum, StrEnum, auto


class Direction(Enum):
    NORMAL = auto
    PRIME = auto  # noqa: PIE796
    DOUBLE = auto  # noqa: PIE796


class Face(StrEnum):
    RIGHT = "R"
    LEFT = "L"
    FRONT = "F"
    BACK = "B"
    UP = "U"
    DOWN = "D"
