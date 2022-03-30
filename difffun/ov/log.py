from .differentiable_function import DifferentiableFunction, T
import math
from .pow import Pow


class Log(DifferentiableFunction):
    @property
    def name(self):
        return "log"

    def forward(self, arg: float) -> float:
        return math.log(arg)

    def derivative(self) -> T:
        return Pow(-1.0)


log = Log()
