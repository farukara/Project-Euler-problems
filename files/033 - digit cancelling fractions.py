#!python3
# coding: utf-8
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#https://projecteuler.net/problem=33

from fractions import Fraction
from math import prod

list_of_fractions = []
for i in range(10, 100):
    for j in range(i+1, 100):
        if str(i)[0] == str(j)[0] or str(i)[0] == str(j)[1]:
            same_digit = str(i)[0]
        elif str(i)[1] == str(j)[0] or str(i)[1] == str(j)[1]:
            same_digit = str(i)[1]
        else:
            same_digit = None
        if same_digit and i%10 !=0: #includes pairs with same digit excludes trivial ones
            if str(i)[0] == str(i)[1]:
                new_i = int(str(i)[0])
            else:
                new_i = i
                new_i = int(str(new_i).replace(same_digit, ""))
            #print("new_i: ", new_i)
            if str(j)[0] == str(j)[1]:
                new_j = int(str(j)[0])
            else:
                new_j = j
                new_j = int(str(new_j).replace(same_digit, ""))
            #print("new_j: ", new_j)
            if new_j == 0 or new_i == 0:
                pass
            elif Fraction(i, j) == Fraction(new_i, new_j):
                list_of_fractions.append(Fraction(i,j))
print()
print(prod(list_of_fractions))
