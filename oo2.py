import math
import re

class Vector(object):
    def __init__(self, *largs):
        self.components = list(largs)
    
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(map(str,self.components)))

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise TypeError("Can't add vectors of different lengths")
        comps = [a+b for a,b in zip(self.components, other.components)]
        return self.__class__(*comps)

    def __mul__(self, scalar):
        return self.__class__(*[x*scalar for x in self.components])

    def __abs__(self):
        return math.sqrt(sum([x**2 for x in self.components]))

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise TypeError("Can't add vectors of different lengths")
        return sum([x*y for x,y in zip(self.components, other.components)])


class Vector3D(Vector):
    type = "Cartesian"

    def __init__(self, i, j, k):
        super(Vector3D, self).__init__(i, j, k)

    @classmethod
    def from_string(cls, st):
        st = st.replace(" ","")
        r = re.compile(r'(-?[0-9]+)i([+-][0-9]+)j([+-][0-9]+)k')
        return cls(*map(int, r.search(st).groups()))
        
    

    # Decorator method of creating properties
    @property
    def i(self):
        return self.components[0]

    @i.setter
    def i(self, val):
        self.components[0] = val

    # Function call method for creating properties
    def get_j(self):
        return self.components[1]

    def set_j(self, val):
        self.components[1] = val

    j = property(get_j, set_j)

    @property
    def k(self):
        return self.components[2]


class Borg(object):
    "All Borg objects will share the same internal state"
    shared_state = {}
    def __init__(self):
        self.__dict__ = Borg.shared_state


class AttributeDictionary(dict):
    "What does this do? And how?"
    def __init__(self):
        self.__dict__ = self


class Something(object):
    foo  = 1
    bar  = 2
