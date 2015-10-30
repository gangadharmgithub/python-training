import unittest

class TestCase1(unittest.TestCase):
    def test_something1(self):
        pass

    def test_something2(self):
        pass

    def test_something3(self):
        pass

    def helper1(self):
        pass


class TestCase2(object):
    def test_something2(self):
        pass

    def helper2(self):
        pass

def main():
    count = 0
    for k1,v1 in globals().items():
        try:
            if issubclass(v1, unittest.TestCase):
                print "Class : {}".format(k1)
                for k2, v2 in v1.__dict__.items():
                    if k2.startswith("test_"):
                        print "   {}".format(k2)
                        count +=1
        except TypeError:
            pass
    print "Found {} testcases".format(count)

    


if __name__ == '__main__':
    main()



