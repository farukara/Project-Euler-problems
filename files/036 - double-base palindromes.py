#!python3
# coding: utf-8
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#https://projecteuler.net/problem=36


from time import perf_counter
from typing import Union

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.2f} seconds")
        return result
    return wrapper

def is_palindromic(n: Union[int, str]) -> bool:
    "returns True if n is palindromic"
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False
    return True

@timeit
def main():
    total = 0 
    for i in range(1_000_000):
        if is_palindromic(i) and (is_palindromic(str(bin(i))[2:])):
            total += i
    print("\n", total)

if __name__ == "__main__":
    main()
