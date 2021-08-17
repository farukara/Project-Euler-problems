#!python3
# coding: utf-8
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
#https://projecteuler.net/problem=34

from time import perf_counter
from math import factorial
from typing import List
from multiprocessing import Process, Queue, cpu_count

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

def isSumOfFactorials(n, factorial_table):
    "returns True if n is sum of factorials of its digits"
    sumofFact = 0 
    for digit in str(n):
        sumofFact += factorial_table[int(digit)]
    return sumofFact == n

def sumOfmagicnumbers2(lower, upper, factorial_table, que) -> int:
    "returns sum of numbers lower and upper that are \
    sum of factorial of their digits, including 1 and 2"
    sum_of_numbers = 0
    for i in range(lower, upper):
        if isSumOfFactorials(i, factorial_table):
            sum_of_numbers += i
    que.put(sum_of_numbers)

@timed
def main():
    factorial_table = {}
    for i in range(10):
        factorial_table[i] = factorial(i)
    limit = 1_000_000 #mathematically upper bound

    sizeOfSlice = limit//cpu_count()
    slices = []
    for i in range(cpu_count()):
        slices.append([sizeOfSlice*i, sizeOfSlice*(i+1)])

    que = Queue()
    #assuming 4 processors
    p1 = Process(target=sumOfmagicnumbers2, args=(slices[0][0], slices[0][1], factorial_table, que))
    p2 = Process(target=sumOfmagicnumbers2, args=(slices[1][0], slices[1][1], factorial_table, que))
    p3 = Process(target=sumOfmagicnumbers2, args=(slices[2][0], slices[2][1], factorial_table, que))
    p4 = Process(target=sumOfmagicnumbers2, args=(slices[3][0], slices[3][1], factorial_table, que))
    processes = [p1, p2, p3, p4]
    for proces in processes:
        proces.start()
    total = 0
    for proces in processes:
        total += que.get()
        proces.join()
    print("\nSum of the numbers:", total-3) #subtract for 1 and 2 factorials

if __name__ == "__main__":
    main()
