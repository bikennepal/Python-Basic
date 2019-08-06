# generate list with range function
# more about pop method
# index method
# pass list to a function


# numbers=list(range(2,20))
# print(numbers)

# print(numbers.pop())

# print(numbers.index(9, 2))

numbers=list(range(1,10))
def neg(l):
    negtive=[]
    for i in l:
        negtive.append(-i)
    return negtive
print(neg(numbers))

