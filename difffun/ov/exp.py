from .differentiable_function import DifferentiableFunction, T
import math


class Exp(DifferentiableFunction):
    @property
    def name(self):
        return "eхp"

    def forward(self, arg: float) -> float:
        return math.exp(arg)

    def derivative(self) -> T:
        return Exp()


exp = Exp()
