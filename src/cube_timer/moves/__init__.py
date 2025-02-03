"""
Classes que encapsulam algumas logicas dos movimentos do embaralhamento
"""

from .double import DoubleMove as DoubleMove
from .normal import NormalMove as NormalMove
from .prime import PrimeMove as PrimeMove

__all__ = "NormalMove", "PrimeMove", "DoubleMove"
