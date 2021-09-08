
#!python3
# coding: utf-8
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, ( 5 3) = 10 .
# In general,  ( n r) = n !  r !  ( n − r) !  , where r ≤ n , n !  = n × ( n − 1) × .  .  .  × 3 × 2 × 1 , and 0 !  = 1 .
# It is not until n = 23 , that a value exceeds one-million: ( 23 10) = 1144066 .
# How many, not necessarily distinct, values of ( n r) for 1 ≤ n ≤ 100, are greater than one-million?
#https://projecteuler.net/problem=52

from time import perf_counter

def timed(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.4f} seconds")
        return value
    return wrapper

@timed
def main():
    #create a lookup table for factorials up to 100
    factorials = {} 
    factorials[0]= 1
    factorials[1]= 1
    for i in range(2,101):
        factorials[i] = factorials[i-1]*i

    #check combinations and increase the count
    count = 0
    for n in range(2,101):
        for r in range(1, n+1):
            if (factorials[n] / (factorials[r]*factorials[n-r])) > 1_000_000:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
