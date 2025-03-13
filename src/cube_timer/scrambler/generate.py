from .moves import DoubleMove, Move, NormalMove, PrimeMove
from .moves import Face as _Face


def _generate_normal_moves() -> tuple[NormalMove, ...]:
    return tuple(NormalMove(i) for i in _Face)


def _generate_prime_moves() -> tuple[PrimeMove, ...]:
    return tuple(PrimeMove(i) for i in _Face)


def _generate_double_moves() -> tuple[DoubleMove, ...]:
    return tuple(DoubleMove(i) for i in _Face)


def generate_moves() -> tuple[tuple[Move, ...], ...]:
    return (
        _generate_normal_moves(),
        _generate_prime_moves(),
        _generate_double_moves(),
    )
