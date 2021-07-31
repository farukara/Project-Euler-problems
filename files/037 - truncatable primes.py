#!python3
# coding: utf-8
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# Note: 2, 3, 5, and 7 are not considered to be truncatable primes.
#https://projecteuler.net/problem=37

from math import sqrt
from time import perf_counter
from functools import cache, lru_cache

def timed(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.2f} secods")
        return result
    return wrapper    

@cache
def is_prime(n):
    if n < 6:
        if n == 0 or n== 1:
            return False
        elif n == 2 or n == 3 or n == 5:
            return True
    elif n % 2 == 0 or n%3==0 or n%5==0:
        return False
    for i in range(7, int(sqrt(n)+1), 2):
        if n%i == 0:
            return False
    return True

def is_truncatable(n):
    #eleminate number including even digits -> made 2 sec improvement
    for i in str(n):
        if int(i) != 2 and not int(i) % 2:
            return False
    m=n
    if is_prime(m):
        while len(str(m)) >1:
            if is_prime(int(str(m)[1:])):
                m = int(str(m)[1:])
                if m == 0:
                    return False
            else:
                return False
        m=n
        while len(str(m)) >1:
            if is_prime(int(str(m)[:-1])):
                m = int(str(m)[:-1])
            else:
                return False
        return True
    else:
        return False

@timed
def main():
    first_eleven_trunctabels = []
    i = 10
    while len(first_eleven_trunctabels) < 11:
        if is_truncatable(i):
            first_eleven_trunctabels.append(i)
        i += 1
    print("\nSum: ", sum(first_eleven_trunctabels))

if __name__ == "__main__":
    main()
