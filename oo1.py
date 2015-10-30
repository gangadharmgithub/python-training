import abc
import math

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(10)
print c.area()
print c.perimeter()

