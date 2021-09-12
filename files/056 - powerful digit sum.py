
#!python3
# coding: utf-8
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
#https://projecteuler.net/problem=56

from time import perf_counter

def timed(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.2f} seconds")
        return value
    return wrapper

@timed
def main():
    max_sum = 0
    for i in range(101):
        for j in range(101):
            max_sum = max(max_sum, sum([int(x) for x in str(pow(i, j))]))
    print(max_sum)

if __name__ == "__main__":
    main()
