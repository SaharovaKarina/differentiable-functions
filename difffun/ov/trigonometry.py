from differentiable_function import DifferentiableFunction, T
from math import sin, cos
from linear import Linear


class Sin(DifferentiableFunction):
    @property
    def name(self):
        return "sin"

    def forward(self, arg: float) -> float:
        return sin(arg)

    def derivative(self) -> T:
        return Cos()


class Cos(DifferentiableFunction):
    @property
    def name(self):
        return "cos"

    def forward(self, arg: float) -> float:
        return cos(arg)

    def derivative(self) -> T:
        return Linear(-1.0)(Sin())
