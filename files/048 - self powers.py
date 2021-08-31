#!python3
# coding: utf-8
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
#https://projecteuler.net/problem=48

from time import perf_counter

def timeit(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.2f} seconds")
        return value
    return wrapper

@timeit
def main():
    total = 0
    for i in range(1, 1001):
        total += pow(i,i)
    print(str(total)[-10:])


if __name__ == "__main__":
    main()
