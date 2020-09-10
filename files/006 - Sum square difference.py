#! Python3
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# https://projecteuler.net/problem=6

goal = 100 
sum_of_sq = 0
summ = 0 
for i in range(1, goal+1):
    sum_of_sq += (i*i)
    summ += i
sq_of_sum = summ**2

print('sum of the squares: ', sum_of_sq)
print('square of the sum: ', sq_of_sum)
print('difference: ', sq_of_sum - sum_of_sq)
