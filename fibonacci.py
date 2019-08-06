# lets put logic in fibnocci sequence


def fib_seq(n):
    a=0
    b=1
    if n == 1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for n in range(n-2):
            c=a+b
            a=b
            b=c
            print(b, end = " ")

fib_seq(10)