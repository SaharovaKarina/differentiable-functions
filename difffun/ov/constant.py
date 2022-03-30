from .differentiable_function import DifferentiableFunction, T


class Constant(DifferentiableFunction):
    def __init__(self, value: float):
        self.value = value

    @property
    def name(self):
        return "constant"

    def __str__(self):
        return str(self.value)

    def forward(self, arg: float) -> float:
        return self.value

    def derivative(self) -> T:
        return Constant(0.0)
