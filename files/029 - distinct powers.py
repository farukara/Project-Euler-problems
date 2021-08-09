#!python3
# coding: utf-8
# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
# 
# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
# 
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# 
# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
#https://projecteuler.net/problem=29

from time import perf_counter
import matplotlib.pyplot as plt
from math import log

def using_set(limit):
    seq = set()
    for i in range(2,limit):
        for j in range(2,limit):
            seq.add(i**j)
    #print(len(seq))

def using_list(limit):
    l = []
    for a in range(2,limit):
        for b in range (2,limit):
            c = a**b
            if c not in l:
                l.append(c)
    #print(len(l))

yset = []
ylist = []
xline = []
i = 1
while i < 101:
    start = perf_counter()
    using_set(i)
    end = perf_counter()
    yset.append(end - start)
    xline.append(i)

    start = perf_counter()
    using_list(i)
    end = perf_counter()
    ylist.append(end-start)
    i += (i+int(log(i)))
    print(i)
plt.plot(xline, yset, label="set")
plt.plot(xline, ylist, label="list")
plt.xlabel("number of items")
plt.ylabel("time (seconds)")
plt.title("Set vs List time performance")
plt.legend()
plt.show()
