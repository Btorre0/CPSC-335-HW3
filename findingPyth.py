# Design an exhaustive search or optimization algorithm that solves the problem below.
# Describe your algorithm with clear pseudocode and prove the time efficiency class of your algorithm, using step counts
# Pythagorean triple problem

# Input: two positive integers a, b with a < b 
# output: a Pythagorean triple (x,y,z) such that x,y and z are positive integers, a ≤ x ≤ y ≤ z ≤ b, and x^2 + y^2 = z^2, or None if no such triple exists

def pythagorean_triple(a, b):
    for x in range(a, b + 1):
        for y in range(x, b +1):
            for z in range(y, b + 1):
                if x**2 + y**2 == z**2:
                    return (x, y, z)
    return None

# Test the function
print(pythagorean_triple(1, 10))
print(pythagorean_triple(10, 30))