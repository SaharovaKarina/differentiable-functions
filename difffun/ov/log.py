from differentiable_function import DifferentiableFunction, T
from math import log
from pow import Pow


class Log(DifferentiableFunction):
    @property
    def name(self):
        return "log"

    def forward(self, arg: float) -> float:
        return log(arg)

    def derivative(self) -> T:
        return Pow(-1.0)
