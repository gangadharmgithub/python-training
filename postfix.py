from operator import add, sub, mul, div

def postfix(exp):
    "Evaluates the postfix expression exp"
    stack = []
    for i in exp:
        if i.isdigit():
            stack.append(int(i))
        else:
            a, b = stack.pop(), stack.pop()
            operations = {'+' : add,
                          '-' : sub,
                          '*' : mul,
                          '/' : div}
            ret = operations[i](b, a)
            stack.append(ret)
    return stack.pop()
