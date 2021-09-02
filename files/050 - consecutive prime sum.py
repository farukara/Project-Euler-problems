#! python3
# coding: utf-8
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# https://projecteuler.net/problem=50

from time import perf_counter
from functools import cache, lru_cache
import numpy as np

def get_prime_sieve(n):
    "return True if index is prime"
    sieve = [True]*(n+1)
    for i in range(2, len(sieve)):
        if sieve[i]:
            k=2
            while (prod := i*k) <= n:
                sieve[prod] = False
                k += 1
    sieve[0] = False
    sieve[1] = False
    return sieve

def list_of_primes(n):
    "Returns list of primes less than n+1"
    primes = []
    sieve = get_prime_sieve(n+1)
    for i in range(n+1):
        if sieve[i]:
            primes.append(i)
    return primes


@cache
def find_longest(limit):
    global longest_sum_prime, lengt_of_seq
    start = perf_counter()
    primes = list_of_primes(limit)
    sieve = get_prime_sieve(limit)
    print("\nTime: ", perf_counter() - start, '\n')
    sum_of_seq = 0
    i = 0
    while i < len(primes) - lengt_of_seq:
    #for i in range(len(primes)-lengt_of_seq):
        localsum = primes[i]
        for j in range(i+1+lengt_of_seq, len(primes)):
            if localsum > limit or not sieve[localsum]:
                continue
            locallen = j-i
            #if localsum in primes:
            if locallen > lengt_of_seq:
                sum_of_seq = localsum
                lengt_of_seq = locallen
                longest_sum_prime = localsum
            localsum += j #sum(primes[i:j])
        i += 1
    return longest_sum_prime, lengt_of_seq

def main():
    start = perf_counter()
    global longest_sum_prime, lengt_of_seq
    longest_sum_prime = 0
    lengt_of_seq = 0
    print(f"\nLongest sum of consecutive primes is: {find_longest(1_0_0)}")
    print(f"Lengt of seq is :", lengt_of_seq)
    print("\nTime: ", perf_counter() - start)

if __name__ == "__main__":
    main()
