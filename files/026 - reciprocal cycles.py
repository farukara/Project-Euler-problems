#!python3
# coding: utf-8
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#https://projecteuler.net/problem=26

from decimal import Decimal, getcontext
from time import perf_counter
import re

def finding_repeat(text, matched_text):
    mo = re_comp.findall(text)
    if mo:
        matched_text = max(mo)
        #to avoid  greedy match
        matched_text = finding_repeat(matched_text, matched_text)
    return matched_text

start = perf_counter()
getcontext().prec = 2048 #sets precision for deciamal class, somehow 2^n works better
ultimategoal  = 0
digit = 1
re_comp = re.compile(r"(.+)\1$") #avoiding multiple compiles

for i in range(2, 1001):
    if i%2 == 0 or i%5 == 0: #mathmatically, those numbers dont have repeating parts
        pass
    else:
        decimal_part = str(Decimal(1) / i).split(".")[1][:-1]
        longest = ''
        longest = finding_repeat(decimal_part, longest)
        
        if len(longest) > ultimategoal:
            ultimategoal = len(longest)
            digit = i

print(f'Digit: {digit}\nLength of sequence: {ultimategoal}')
print('Time: ', perf_counter() - start)
