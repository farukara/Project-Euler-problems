#!python3
# coding: utf-8
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#https://projecteuler.net/problem=52

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
    power = 0
    found = False
    while not found :
        for i in range(pow(10, power), pow(10, power+1)//6+1): #only need to check 1/6 of each 10power group
            numlist = sorted(list(str(i)))
            if sorted(str(2*i)) == numlist and sorted(str(3*i)) == numlist and sorted(str(4*i)) == numlist and sorted(str(5*i)) == numlist and sorted(str(6*i)) == numlist: #chained to help short circuiting
                print(i, i*2, i*3, i*4, i*5, i*6)
                found = True
                break #early break for for loop
        power += 1



if __name__ == "__main__":
    main()
