import abc
import math

class Shape(object):
    """Defines the Shape interface.
    Abstract base class.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def foo(self):
        return self.area() + self.perimeter()

class Ellipse(Shape):
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    
    def area(self):
        return math.pi * self.major * self.minor
        

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.major**2 + self.minor**2)/2)

class Circle(Ellipse):
    def __init__(self, radius):
        self.radius = radius
        import pdb; pdb.set_trace()
        super(Circle, self).__init__(radius, radius)

c = Circle(4)
print c.area()
print c.perimeter()


# Liskov substitution principle

class MyException(Exception):
    pass


