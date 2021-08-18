#!python3
# coding: utf-8
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#https://projecteuler.net/problem=34

from time import perf_counter

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.2f} seconds")
        return result
    return wrapper 

def get_prime_sieve(n):
    "return True if index is prime"
    sieve = [True]*(n+1)
    for i in range(2, n+1):
        if sieve[i]:
            k=2
            while (prod := i*k) <= n:
                sieve[prod] = False
                k += 1
    sieve[0] = False
    sieve[1] = False
    return sieve

def is_circular_prime(n):
    "return True if n is circular prime"
    if not sieve[n]:
        return False
    for i in str(n):
        if i in list("024568"):
            return False
    n = str(n)
    for i in range(len(n)):
        n = n[1:]+n[0]
        if not sieve[int(n)]:
            return False
    return True
    
@timeit
def main():
    global sieve
    count = 0
    n = 1_000_000
    sieve = get_prime_sieve(n)
    for i in range(3, n, 2):
        if is_circular_prime(i):
            count += 1
    print("\n", count+2) # +2 is for "2" and "5"

if __name__ == "__main__":
    main()
