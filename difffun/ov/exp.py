from differentiable_function import DifferentiableFunction, T
from math import exp


class Exp(DifferentiableFunction):
    @property
    def name(self):
        return "exp"

    def forward(self, arg: float) -> float:
        return exp(arg)

    def derivative(self) -> T:
        return Exp()
