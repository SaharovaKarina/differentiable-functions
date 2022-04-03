from .differentiable_function import DifferentiableFunction, T
from .constant import Constant


class Linear(DifferentiableFunction):
    def __init__(self, coefficient: float):
        self.coefficient = coefficient

    def __str__(self):
        return f"{self.coefficient} * x"

    @property
    def name(self):
        return "linear"

    def forward(self, arg: float) -> float:
        return self.coefficient * arg

    def derivative(self) -> T:
        return Constant(self.coefficient)
