"""
Exercises for Day 1 of the intermediate-advanced python
training course at Virident.
"""
def tables(n):
    """
    Prints times tables of given n from 1 to 10.
    """
    for i in range(1, 11):
        print "{} x {} = {}".format(i, n, i*n)

def good_tables(n):
    """
    Prints times tables of given n from 1 to 10.
    """
    vals = []
    for i in range(1, 11):
        vals.append("{} x {} = {}".format(i, n, i*n))
    return vals

def fizzbizz(n):
    """
    Jeff Atwood (@codinghorror's) famous Fizz Bizz test implemented
    in python.
    """
    for i in range(1, n+1):
        if i%15 == 0:
            print "fizzbizz"
        elif i%5 == 0:
            print "bizz"
        elif i%3 == 0:
            print "fizz"
        else:
            print i

def palindrome(s):
    """
    Will return True if is a palindrome.
    
    palindrome("abba") == True
    palindrome("bolton") == False
    """
    return s == s[::-1]

def panagram(s):
    """
    Will return true for sentences like

    "the quick brown fox jumps over the lazy dog" &
    "sphinx of black quartz, judge my vow"
    
    which contain all letters of the alphabet.
    """
    s = s.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True

def freq(s):
    """
    Prints a frequency count of all letters in the given string
    """
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for k,v in d.items():
        print "{} :: {}".format(k,v)

    
def postfix(exp):
    "Evaluates the postfix expression exp"
    stack = []
    for i in exp:
        if i.isdigit():
            stack.append(int(i))
        else:
            a, b = stack.pop(), stack.pop()
            if i == "+":
                stack.append(a + b)
            if i == "-":
                stack.append(b - a)
            if i == "*":
                stack.append(a * b)
            if i == "/":
                stack.append(b / a)
    return stack.pop()


def primes(n):
    """
    Should return the prime numbers from 1 to n

    Doesn't use %.
    """
    ret = []
    cancelled = set()
    for i in range(2, n+1):
        if i not in cancelled:
            ret.append(i)
            for j in range(i, n+1, i):
                cancelled.add(j)
    return ret

def factorise(n):
    """
    Return a list of prime factors of n
    factorise(100) => [2, 2, 5, 5]
    """
    pass

def my_map(fn, iterable):
    ret = []
    for i in iterable:
        ret.append(fn(i))
    return ret

def my_filter(pred, iterable):
    ret = []
    for i in iterable:
        if pred(i):
            ret.append(i)
    return ret

# Comprehensions
t = [x**2 for x in range(100) if x%2 == 0]
d = dict(x = 1, y = 2, z = 3) 
{v:k for k,v in d.items()} # => {1: 'x', 2: 'y', 3: 'z'}
{k[:10]:len(k) for k in open("/etc/passwd")}

def memoise(original_function):
    original_function.cache = {}
    def memoised_function(*largs, **kargs):
        key = largs + tuple(kargs.items())
        if key in original_function.cache:
            return original_function.cache[key]
        else:
            ret = original_function(*largs, **kargs)
            original_function.cache[key] = ret
            return ret
    return memoised_function


def count(original_fn):
    def counted_fn(n):
        ret = original_fn(n)
        counted_fn.count += 1
        return ret
    counted_fn.count = 0
    return counted_fn

def trace(fn):
    fn.depth = -1
    def traced_fn(n):
        fn.depth += 1
        print fn.depth * "|   " + "+---{}({})".format(fn.__name__, n)
        ret = fn(n)
        print fn.depth * "|   " + "`---ret : {}".format(ret)
        fn.depth -= 1
        return ret
    return traced_fn

# 10.132.4.20 
# fib = memoise(fib)

@trace
@memoise
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@trace
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


## Types of arguments and argument passing
def add(x, y = 1):
    "Will add x to y. y defaults to 1"
    return x + y

def raise_to(base, power):
    return base ** power

raise_to(5, 2) # Calling by position (base = 5 and power = 2)

raise_to(power = 2, base = 5) # Calling by keyword (base =5, power =2)

def sum(*largs): # Variable number of positional arguments
    total = 0
    for i in largs:
        total += i
    return total

def create_dict(**kargs):
    print kargs
    ret = dict()
    for k,v in kargs.items():
        ret[k] = v
    return ret

def super_function(name, age, *largs, **kargs):
    print name
    print age
    print largs
    print kargs
    
t = [1,2] 
add(*t)  # Applying positional arguments and calling add

t= dict(x=1, y = 2)
add(**t) # Applying keyword arguments and calling add


