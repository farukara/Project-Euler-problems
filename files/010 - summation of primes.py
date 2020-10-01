#! Python3
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
# https://projecteuler.net/problem=10

import sympy

summ = 0
i = 0 
while i <= 2_000_000:
   if sympy.isprime(i):
        summ += i
    i += 1
print(summ)
