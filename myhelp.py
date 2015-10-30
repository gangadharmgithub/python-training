import types

def foo():
    "my docstring"
    pass

def no_docstring():
    pass

class A(object):
    """Class docstring comes here"""

    def documented(self):
        "I am a documented function"
        pass

    def undocumented(self):
        pass

def myhelp(obj):
    """
    A stripped down version of the inbuilt help.
    - Poorer formatting
    - Works only for functions and classes (no objects)
    """
    if isinstance(obj, types.FunctionType):
        print "{}()".format(obj.__name__)
        if obj.__doc__:
            print "   {}".format(obj.__doc__)
    elif isinstance(obj, types.TypeType):
        print "Class {}".format(obj.__name__)
        if obj.__doc__:
            print "   {}".format(obj.__doc__)
        print ""
        # Print member docstrings
        for attrname in dir(obj):
            attr = getattr(obj, attrname)
            if isinstance(attr, types.UnboundMethodType):
                print "   method {}()".format(attr.__name__)
                if attr.__doc__:
                    print "      {}".format(attr.__doc__)
                    print ""
    elif isinstance(obj, types.ModuleType):
        print "Module {}".format(obj.__name__)
        if obj.__doc__:
            print "   {}".format(obj.__doc__)
        print ""
        for attrname in dir(obj):
            attr = getattr(obj, attrname)
            myhelp(attr)

# 10.132.4.20            
            
    
if __name__ == '__main__':
    myhelp(A)
