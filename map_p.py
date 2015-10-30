def func(n):
    #your code here
    li = []
    for i in n:
        try:
            i =  int(i)
        except Exception:
            return "arry ele"
        
        if i % 2 == 0:
            print True
            li.append(True)
        else:
            print False
            li.append(False)

    return li
        
            
    #return [v for v in n if v == int(v) else "given argument is not a function"]

def map(arr, somefunction):
    #your code here
    #note: Python already supports all this, we are just rewriting our own
    #map() function with some quirk and error message
    if not hasattr(somefunction, '__call__') : return "given argument is not a function"
    return somefunction(arr)

print map([3,'j',-4], func)
print map([-3,10,2], func)
