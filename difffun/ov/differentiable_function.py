from abc import ABCMeta
from .base import DifferentiableFunctionBase, T
from .binary_operation import Plus, Minus, Mul, Composition


class DifferentiableFunction(DifferentiableFunctionBase, metaclass=ABCMeta):
    def __add__(self, other: T) -> T:
        return Plus(self, other)

    def __sub__(self, other: T) -> T:
        return Minus(self, other)

    def __mul__(self, other: T) -> T:
        return Mul(self, other)

    def __call__(self, other: T) -> T:
        return Composition(self, other)
