
def set_difference(L, R):
    elements_r = set(R)
    result = []
    for x in L:
        if x not in elements_r:
            result.append(x)
    return result

# test the function
print(list(set_difference([1, 2, 3], [3, 4, 5])))
print(list(set_difference([1, 2, 3], [4, 5, 6])))
print(list(set_difference([1, 2, 3], [1, 2, 3])))