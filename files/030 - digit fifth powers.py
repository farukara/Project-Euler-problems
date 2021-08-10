#!python3
# coding: utf-8
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#https://projecteuler.net/problem=30

from time import perf_counter

def timed(function):
    "decorator for time performance of function"
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        fname = function.__name__
        print(f"\n{fname} function took {finish - start:.2f} seconds")
        return value

    return wrapper

@timed
def digit_fifth_powers(power):
    "prints grand total of numbers that equals total of it's digits raised to power"
    limit = (6*(9**power))+1 #6 is hard coded bc no number above 6 digit can satisfy the req
    grand_total = 0
    for i in range(2, limit):
        total = 0 
        for digit in str(i):
            total += int(digit)**power
        if total == i:
            #print(i)
            grand_total += i

    print("\nGrand total: ", grand_total)

if __name__ == "__main__":
    digit_fifth_powers(5)
