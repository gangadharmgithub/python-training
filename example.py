# Example of decorators with arguments


@numba.jit
def foo():
    for i in range(1000):
        print i
                   

def banner(char):
    def banner_decorator(fn):
        def decorated_fn(n):
            print 50*char
            ret = fn(n)
            print 50*char
            return ret
        return decorated_fn
    return banner_decorator
        

@banner("-")
def tables(n):
    for i in range(1, 11):
        print "{} x {} = {}".format(n, i, n*i)



tables(5)

@repeat(max = 10, backoff = 5)
@memoise(cache_size = 100, expire = 10, store = "redis")
@require(group = "admin")
@require_login


