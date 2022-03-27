from abc import ABCMeta, abstractmethod


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
    def derivative(self, arg: float) -> float:
        """Gives f'(x)"""
