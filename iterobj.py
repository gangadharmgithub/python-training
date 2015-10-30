class Example(object):
    def __init__(self, n):
        self.components = ["Hello {}".format(i) for i in range(n)]
        self.index = 0

    def __iter__(self):
        for i in self.components:
            yield i
        
        


e = Example(10)

for i in e:
    print i
