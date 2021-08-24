#!python3
# coding: utf-8
# We shall say that an *n*-digit number is pandigital if it makes use of all the digits 1 to *n* exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest *n*-digit pandigital prime that exists?
#https://projecteuler.net/problem=30

from time import perf_counter
from itertools import permutations
from math import sqrt

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.2f} seconds")
        return result
    return wrapper

def is_prime(n):
    "return True if n is prime"
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

@timeit
def main():
    #dropped 8 and 9 b/c a number is divisible by 3 if 
    #sum of its digits is divisible by 3

    pan_digits = list("1234567") 
    candidates = []
    for i in range(9):
        pan_digits = pan_digits[:9-i]
        combs = permutations(pan_digits, len(pan_digits))
        for comb in combs:
            if is_prime(int("".join(comb))):
                candidates.append(int("".join(comb)))
        if candidates: #early exit
            break
    print(max(candidates))

if __name__ == "__main__":
    main()
