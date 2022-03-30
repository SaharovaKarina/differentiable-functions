import re
from .base import BinaryOperation, T


class Plus(BinaryOperation):
    @property
    def symbol(self) -> str:
        return "+"

    def forward(self, arg: float) -> float:
        return self.left.forward(arg) + self.right.forward(arg)

    def derivative(self) -> T:
        return Plus(self.left.derivative(), self.right.derivative())


class Minus(BinaryOperation):
    @property
    def symbol(self) -> str:
        return "-"

    def forward(self, arg: float) -> float:
        return self.left.forward(arg) - self.right.forward(arg)

    def derivative(self) -> T:
        return Minus(self.left.derivative(), self.right.derivative())


class Mul(BinaryOperation):
    @property
    def symbol(self) -> str:
        return "*"

    def forward(self, arg: float) -> float:
        return self.left.forward(arg) * self.right.forward(arg)

    def derivative(self) -> T:
        return Plus(
            Mul(self.left.derivative(), self.right),
            Mul(self.left, self.right.derivative())
        )


class Composition(BinaryOperation):
    def __str__(self):
        return re.sub("x", self.right.__str__(), self.left.__str__())

    @property
    def symbol(self) -> str:
        return "o"

    def forward(self, arg: float) -> float:
        """left(right(x))"""
        return self.left.forward(self.right.forward(arg))

    def derivative(self) -> T:
        """left'(right(x)) * right'(x)"""
        return Mul(Composition(self.left.derivative(), self.right), self.right.derivative())
