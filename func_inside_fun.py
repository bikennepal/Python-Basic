def greater(a,b):
    if a > b:
        return a
    return b


def greates(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

def new_greaterst(a,b,c):
        bigger=greater(a,b)
        return greater(bigger,c)


print(new_greaterst(30,50,60))