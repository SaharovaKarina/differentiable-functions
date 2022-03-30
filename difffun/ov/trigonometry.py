from .differentiable_function import DifferentiableFunction, T
import math
from .linear import Linear


class Sin(DifferentiableFunction):
    @property
    def name(self):
        return "sin"

    def forward(self, arg: float) -> float:
        return math.sin(arg)

    def derivative(self) -> T:
        return Cos()


class Cos(DifferentiableFunction):
    @property
    def name(self):
        return "cos"

    def forward(self, arg: float) -> float:
        return math.cos(arg)

    def derivative(self) -> T:
        return Linear(-1.0)(Sin())


sin = Sin()
cos = Cos()
