from abc import ABCMeta, abstractmethod
from typing import Union

T = Union['DifferentiableFunctionBase', 'BinaryOperation']


class DifferentiableFunctionBase(metaclass=ABCMeta):
    def __str__(self):
        return f"{self.name}(x)"

    @property
    def name(self):
        return "f"

    @abstractmethod
    def forward(self, arg: float) -> float:
        """Gives f(x)"""

    @abstractmethod
    def derivative(self) -> T:
        """Gives f'(x)"""


class BinaryOperation(metaclass=ABCMeta):
    def __init__(self, left: T, right: T):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left.__str__()} {self.symbol} {self.right.__str__()}"

    @property
    @abstractmethod
    def symbol(self) -> str:
        """Examples are +-*/"""

    @abstractmethod
    def forward(self, arg: float) -> float:
        """Gives bin(left(x), right(x))"""

    @abstractmethod
    def derivative(self) -> T:
        """Gives D[bin(left(x), right(x))]"""
