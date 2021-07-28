#!python3
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#https://projecteuler.net/problem=21

from time import perf_counter
from math import sqrt

def proper_divisors(n):
    'returns a list of proper divisors of number n'
    divisor_list = [1]
    i=2
    while i < int(sqrt(n)+1):
        if n % i == 0:
           divisor_list.append(i)
           if i != n/i:
               divisor_list.append(n//i)
        i += 1
    return divisor_list

def are_amicable(n,m):
    'returns True if 2 numbers are amicable'
    if all([
            sum(proper_divisors(n)) == m,
            sum(proper_divisors(m)) == n,
            n != m 
            ]):
        return True
    else:
        return False

if __name__ == "__main__":
    start = perf_counter()
    amilist = []
    for i in range(10_000):
        if are_amicable(i, sum(proper_divisors(i))):
            amilist.append(i)
    print('list of amicable numbers: ', amilist)
    print('sum of the amicable numbers: ', sum(amilist))
    print("Time: ", perf_counter() - start)
