# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractclassmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius * self.radius)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side * self.side)


# g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
