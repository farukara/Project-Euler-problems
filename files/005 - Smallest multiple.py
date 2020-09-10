#! Python3 
## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
## https://projecteuler.net/problem=5


# First iteration below is not using any module. That's why the code is processor intensive. Second iteration uses math module to calculate Greatest Common Divisor.


# First iteration without any import for numbers 1-10
i = 10
checker = True

while checker == True:
    i += 1
    multi_list = []
    for x in range(1,11):
        if i%x == 0:
            multi_list.append(True)
        else:
            multi_list.append(False)
    if all(multi_list):
        checker =  False
    else:
        checker = True
print(i)    

# Second iteration using math module for numbers 1-20
import math

lowest_multiplier = 1
for i in range(1, 21):
    lowest_multiplier *= i // math.gcd(i, lowest_multiplier)

print(lowest_multiplier)
