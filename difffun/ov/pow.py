from differentiable_function import DifferentiableFunction, T
from linear import Linear


class Pow(DifferentiableFunction):
    def __init__(self, exponent: float):
        self.exponent = exponent

    def __str__(self):
        return f"x ^ {self.exponent}"

    @property
    def name(self):
        return "pow"

    def forward(self, arg: float) -> float:
        return pow(arg, self.exponent)

    def derivative(self) -> T:
        return Linear(self.exponent)(Pow(self.exponent - 1))
