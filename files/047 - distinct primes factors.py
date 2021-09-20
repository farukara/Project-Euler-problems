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

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, *kwargs)
        end = perf_counter()
        print(f"{func.__name__} function took {end-start:.3f} seconds")
        return result
    return wrapper

def isprime(n):
    "returns True if n is a prime"
    if n ==2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def factors(n):
    "returns set of int factors"
    set_of_factors = set()
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            set_of_factors.add(i)
            set_of_factors.add(int(n/i))
    return set_of_factors

@cache
def has_prime_factors(number, count):
    "return True if number has -count- factors"
    global primelist
    divisor_list = factors(number)
    prime_factors = set()
    for divisor in divisor_list:
        if divisor in primelist:
            prime_factors.add(divisor)
        elif isprime(divisor):
            prime_factors.add(divisor)
            primelist.add(divisor)
    if len(prime_factors) < count:
        return False
    if prime_factors:
        for i in range(count, len(divisor_list)+1):
            for cmb in combwr(prime_factors, i):
                if number == prod(cmb) and len(set(cmb)) == count:
                    #print(cmb)
                    return True
    else: 
        return False
    

@timeit
def main():
    global primelist
    primelist = set()
    i = 1
    count = 3
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
