#  offline ski rental
# input: a daily ski rental price r > 0,
# purchase price p > 0, 
# and number of days d>0 output: True if it is cheaper to rent skis
# for d days at r dollars per day, or False if 
# it is cheaper to buy skis for p dollars

def skiRental(r, p, d):
    rental_cost = r * d
    if rental_cost < p:
        return True
    else:
        return False
    

print(skiRental(20, 300, 10))
print(skiRental(20, 300, 20))
print(skiRental(20, 300, 15))
print(skiRental(20, 300, 5))
print(skiRental(20, 300, 0))
