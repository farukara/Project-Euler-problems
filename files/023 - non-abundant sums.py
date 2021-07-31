#! Python3
# coding: utf-8
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# https://projecteuler.net/problem=23

from time import perf_counter
from math import sqrt
def sum_proper_divisors(n):
    'returns sum of proper divisors of number n'
    divisor_list = [1]
    i=2
    while i < int(sqrt(n)+1):
        if n % i == 0:
           divisor_list.append(i)
           if i != n/i:
               divisor_list.append(n//i)
        i += 1

    return sum(divisor_list)

def is_abundant(n):
    "returns True if n is abundant number"
    return sum_proper_divisors(n) > n

def is_sum_of_2_abundant(n):
    "returns True if n can be written as sum of 2 abundant numbers"
    for i in range(12, n):
        if maskisabundant[i] and maskisabundant[n-i]:
            return True
    return False

if __name__ == "__main__":
    start = perf_counter()
    upper_limit = 28124
    total = 0
    # create a mask for abundant numbers to avoid redundant computations
    maskisabundant = [0]* upper_limit
    for i in range(1, upper_limit):
        if is_abundant(i):
            maskisabundant[i] = 1
    for i in range(upper_limit):
        if not is_sum_of_2_abundant(i):
            total += i
    print(total)
    print("Time: ", perf_counter() - start)
