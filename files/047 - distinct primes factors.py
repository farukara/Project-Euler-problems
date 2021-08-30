#!python3
# coding: utf-8
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
#https://projecteuler.net/problem=47

from math import sqrt, prod
from time import perf_counter
from itertools import combinations_with_replacement as combwr
from functools import cache, lru_cache

def isprime(n):
    "returns True if n is a prime"
    if n ==2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def divisors(n):
    "returns set of int divisors"
    set_of_divisors = set()
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            set_of_divisors.add(i)
            set_of_divisors.add(int(n/i))
    return set_of_divisors

@cache
def has_prime_factors(number, count):
    "return True if number has -count- factors"
    global primelist, numbers_dont_have_primefactors
    if number in numbers_dont_have_primefactors:
        return False
    divisor_list = divisors(number)
    prime_divisors = set()
    for divisor in divisor_list:
        if divisor in primelist:
            prime_divisors.add(divisor)
        elif isprime(divisor):
            prime_divisors.add(divisor)
            primelist.add(divisor)
    if len(prime_divisors) < count:
        numbers_dont_have_primefactors[number] = number
        return False
    if prime_divisors:
        for i in range(count, len(divisor_list)+1):
            for cmb in combwr(prime_divisors, i):
                if number == prod(cmb) and len(set(cmb)) == count:
                    #print(cmb)
                    return True
    else: 
        numbers_dont_have_primefactors[number] = number
        return False
    
def main():
    global primelist, numbers_dont_have_primefactors 
    primelist = set()
    numbers_dont_have_primefactors = dict()
    i = 1
    count = 4
    while True:
        conditions = []
        for j in range(count):
            if has_prime_factors(i+j, count):
                conditions.append(True)
            else:
                conditions.append(False)
        if len(conditions) == count and all(conditions):
            print("\nfound: ", end="")
            for k in range(count):
                print(i+k, end=",")
            print()
            break
        i += 1

if __name__ == "__main__":
    start = perf_counter()
    main()
    print("Time: ", perf_counter() - start)
