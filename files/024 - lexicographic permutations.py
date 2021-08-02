#! Python3
# coding = utf8
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# https://projecteuler.net/problem=24

from itertools import permutations
from time import perf_counter

perms = permutations("0123456789")

i=1
start = perf_counter()
for perm in perms:
    #print(perm)
    if i == 1_000_000:
        print()
        print("".join(perm))
        break
    i += 1

print("Time: ", perf_counter() - start)

