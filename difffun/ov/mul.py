from differentiable_function_base import DifferentiableFunctionBase


class Mul(DifferentiableFunctionBase):
    """Gives f(x) = g(x) * h(x)"""
    def __init__(self, left: DifferentiableFunctionBase, right: DifferentiableFunctionBase):
        self.left = left
        self.right = right

    def forward(self, arg: float) -> float:
        return self.left.forward(arg) * self.right.forward(arg)

    def derivative(self, arg: float) -> float:
        """f'(x) = g'(x)h(x) + g(x)h'(x)"""
        return self.left.derivative(arg) * self.right.forward(arg) + self.left.forward(arg) * self.right.derivative(arg)
