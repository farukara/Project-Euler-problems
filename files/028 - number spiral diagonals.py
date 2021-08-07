#!python3
# coding: utf-8
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#https://projecteuler.net/problem=28

from time import perf_counter

start = perf_counter()
i = 1
diagonals = [i]
while i < 1001:
    m = i+1
    j = diagonals[-1] + m
    for _ in range(4):
        diagonals.append(j) 
        j += m
    i += 2

#print(diagonals)  
print(sum(diagonals))
print("Time: ", perf_counter() - start)
