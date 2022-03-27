import re
from differentiable_function_base import DifferentiableFunctionBase


class Composition(DifferentiableFunctionBase):
    """Gives f(x) = h(g(x))"""
    def __init__(self, parent: DifferentiableFunctionBase, child: DifferentiableFunctionBase):
        self.parent = parent  # h
        self.child = child  # g

    def __str__(self):
        return re.sub("x", self.child.__str__(), self.parent.__str__())

    def forward(self, arg: float) -> float:
        return self.parent.forward(self.child.forward(arg))

    def derivative(self, arg: float) -> float:
        """f'(x) = h'(g(x))g'(x)"""
        return self.parent.derivative(self.child.forward(arg)) * self.child.derivative(arg)
