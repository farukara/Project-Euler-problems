#! Python3
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# https://projecteuler.net/problem=9

found = []
for a in range(1,int(1001/3)):  # a can't be greater than 1000/3 
    for b in range(a,int(1001/2+1)):  # b can't be greater than 1000/2
        c = 1000 - (a+b)
        print(a, b, c)
        if (a**2+b**2) == c**2 and a+b+c == 1000:
           found = [a,b,c]
           break
    if found:
        break
print(found)
prod = found[0]*found[1]*found[2]
print('Product: ', prod)
