# For each of the following problems: 
#     design a reduction algorithm that solves the problem. 
#     Prove the time efficiency class of your algorithm. Hint: Your algorithm should use a hash table or 
#     sorting algorithm.

def set_union(L, R):
    seen = {}
    
    for i in L:
        seen[i] = True
    for i in R:
        seen[i] = True
    return list(seen.keys())

# test the function
print(set_union([1, 2, 3], [3, 4, 5]))
print(set_union([1, 2, 3], [4, 5, 6]))
print(set_union([1, 2, 3], [1, 2, 3]))