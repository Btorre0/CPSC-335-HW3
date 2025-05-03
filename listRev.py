# (b) list reversal
# input: a list L of n elements 
# output: a list containing the elements of L but in reversed order

# using the naive algo
def listRev(L):
    list_l = []
    for i in range(len(L)-1, -1, -1):
        list_l.append(L[i])
    return list_l

# test the function
print(listRev([1, 2, 3]))
print(listRev([1, 2, 3, 4, 5, 6]))

