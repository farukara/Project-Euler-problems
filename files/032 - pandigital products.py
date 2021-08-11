#!python3
# coding: utf-8
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#https://projecteuler.net/problem=30

from time import perf_counter
from typing import Union
from multiprocessing import Process, Queue, Pool

def timed(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.2f} seconds")
        return value
    return wrapper

def isPandigital(number: Union[int,str]) -> bool:
    "returns True if number is 9 digit pandigital"
    number = str(number)
    if len(number) != 9:
        return False
    if "0" in number:
        return False
    if len(set(number)) != 9:
        return False

    return True

def firsthalf(que):
    group = set()
    for i in range(1, 50): #mathmatically possible options for i and j
        if "0" in str(i) or len(str(i)) != len(set(str(i))): #drop bad candidates
            pass
        else:
            for j in range(123, 9877): # little bit math logic to reduce iterations
                number =  str(i) + str(j) + str(i*j)
                if isPandigital(number):
                    group.add(i*j)
    que.put(sum(group))
    #return sum(group)
def secondhalf(que):
    group = set()
    for i in range(50, 99): #mathmatically possible options for i and j
        if "0" in str(i) or len(str(i)) != len(set(str(i))): #drop bad candidates
            pass
        else:
            for j in range(123, 9877): # little bit math logic to reduce iterations
                number =  str(i) + str(j) + str(i*j)
                if isPandigital(number):
                    group.add(i*j)
    que.put(sum(group))
    #return sum(group)
    #print("\nTotal: ", sum(group))

#@timed
def main():
    group = set()
    for i in range(1, 99): #mathmatically possible options for i and j
        if "0" in str(i) or len(str(i)) != len(set(str(i))): #drop bad candidates
            pass
        else:
            for j in range(123, 9877): # little bit math logic to reduce iterations
                number =  str(i) + str(j) + str(i*j)
                if isPandigital(number):
                    group.add(i*j)
    print("\nTotal: ", sum(group))

if __name__ == "__main__":
    #main()
    start = perf_counter()
    Q = Queue()
    #p = Pool(2)
    #first = p.apply(firsthalf)
    #second = p.apply(secondhalf)
    #print(first + second)
    p1 = Process(target=firsthalf, args=(Q,))
    p2 = Process(target=secondhalf, args=(Q,))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
    value1 = Q.get()
    value2 = Q.get()
    print(value1+value2)
    end = perf_counter()
    print("Time: ", end - start)
