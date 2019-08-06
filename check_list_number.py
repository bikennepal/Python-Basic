# to check if common number exist in the list

def lis(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output



print(lis([1,2,3],[1,4,3]))