#!python3
# coding: utf-8
#https://projecteuler.net/problem=63

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
    count = 0
    limit = 30 #found that limit heuristically
    for i in range(1,limit):
        for j in range(1, limit):
            if len(str(pow(i, j))) == j:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
