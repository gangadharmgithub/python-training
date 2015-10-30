# Eager functions

def squares(n):
    ret = []
    for i in range(0, n+1):
        ret.append(i**2)
    return ret

def lazy_squares(n):
    for i in range(0, n+1):
        yield (i ** 2)

def for_looping():
    # How a for loop works
    for i in [1,2,3,4,5]:
        print i

    _i = iter([1,2,3,4,5])
    while True:
        try:
            i = next(_i)
            print i
        except StopIteration:
            break

def lazy_map(fn, iterable):
    for i in iterable:
        yield fn(i)

def lazy_filter(fn, iterable):
    for i in iterable:
        if fn(i):
            yield i

def take_n(iterable, n):
    c = 0
    for i in iterable:
        if c < n:
            c+=1
            yield i
        else:
            break

# take_first - Get the first value that satisfies a condition
# take_while - Get all values as long as a condition is satisfied
# take_until - Get all values till a condition is satisfied

#10.132.4.20

def take_first(predicate, iterable):
    for i in iterable:
        if predicate(i):
            return i

def take_while(predicate, iterable):
    for i in iterable:
        if predicate(i):
            yield i
        else:
            break

def take_until(predicate, iterable):
    for i in iterable:
        if not predicate(i):
            yield i
        else:
            break


def chain(*iterables):
    for iterable in iterables:
        for i in iterable:
            yield i


