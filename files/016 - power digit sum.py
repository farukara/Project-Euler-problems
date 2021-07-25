#! Python3
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# https://projecteuler.net/problem=16

number = 1000

result = 2**number
total = 0
for i in str(result):
    total += int(i)

print (total)
