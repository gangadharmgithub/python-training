import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

# 10.132.4.20


        
        
