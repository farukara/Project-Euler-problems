
#!python3
# coding: utf-8
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
# #https://projecteuler.net/problem=51

from time import perf_counter
from math import sqrt
from itertools import combinations, permutations

def timeit(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.2f} seconds")
        return value
    return wrapper

def is_prime(n):
    "returns True if n is prime, False otherwise"
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

@timeit
def main():
    for number_of_digits in range(2,3): # loops the required number of digits, eg 3 for 100 to 999
        for star_value in range(10): # loops the possible value of stars in the question
            for number_of_stars in range(1, number_of_digits): #loops number of stars in a given number
                for candidate_number in range(pow(10, number_of_digits-1-number_of_stars), pow(10, number_of_digits-number_of_stars)):
                    list_candidate_number = list(str(candidate_number)) + list(str(star_value) * number_of_stars)
                    print(list_candidate_number)
                    combs = permutations(list_candidate_number)
                    for comb in combs:
                        if is_prime(int("".join(comb))):
                            temp_list.append(int("".join(comb)))
                            print(comb)

if __name__ == "__main__":
    main()
