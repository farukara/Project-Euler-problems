#!python3
# coding: utf-8
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
#https://projecteuler.net/problem=38

from time import perf_counter

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.2f} seconds")
        return result
    return wrapper

@timeit
def main():
    for i in range(10_00_000, 1_00_00_000):
        products = []
        for j in range(1, 10):
            products.append(i*j)
            concat = "".join(map(str, products))
            if len(concat) == 9 and len(set(concat)) == 9 and "0" not in concat:
                print("i: ", i)
                print("products: ", products)
                print("concat: ", concat)
                print("integer: ", j)

if __name__ == "__main__":
    main()
