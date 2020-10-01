#! Python3
# What is the value of the first triangle number to have over five hundred divisors?
# https://projecteuler.net/problem=12

target = 500
i = j =  0
result = True
while result:
    divisors, k, l = 0, 1, 1
    j += 1
    i = i+j

    # reducing upper boundery by doubling number of divisors, counting for product of each 
    while k < i/l:  
        k += 1
        if i%k == 0:
            l=k
            divisors += 2
            if divisors >= target:
                result = False
    print(j, i, " divisors: ", divisors)
print("Result: ", i)
            

