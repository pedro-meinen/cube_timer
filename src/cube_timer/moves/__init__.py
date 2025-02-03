"""
Classes que encapsulam algumas logicas dos movimentos do embaralhamento
"""

from .move import Directions as _Directions
from .move import DoubleMove as DoubleMove
from .move import Move as Move
from .move import NormalMove as NormalMove
from .move import PrimeMove as PrimeMove


def _generate_normal_moves() -> tuple[NormalMove, ...]:
    return tuple(NormalMove(i) for i in _Directions)


def _generate_prime_moves() -> tuple[PrimeMove, ...]:
    return tuple(PrimeMove(i) for i in _Directions)


def _generate_double_moves() -> tuple[DoubleMove, ...]:
    return tuple(DoubleMove(i) for i in _Directions)


def generate_moves():
    return _generate_normal_moves(), _generate_prime_moves(), _generate_double_moves()


__all__ = "NormalMove", "PrimeMove", "DoubleMove", "Move"
