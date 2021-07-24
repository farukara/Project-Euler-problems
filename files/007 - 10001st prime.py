#! Python3
# What is the 10 001st prime number?
# https://projecteuler.net/problem=7


# 1st approach: Using python's sympy module. Pretty fast. 
#import sympy
#goal = 10001 # trying to find goal'th prime number
#i = j = 0
#while i < goal:
#    j += 1
#    if sympy.isprime(j):
#        i += 1
#        print(i)
#
#print(i-1, 'th prime number is ', j)


# 2nd aproach (takes about ?): Using sqrt from math module and own writen isprime function: Takes about 2 sec. Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of smaller factor that has been already checked. And also algorith is further optimezed to just chech every 6th number TODO ?????? 

def isprime(number):
    from math import sqrt
    # returns true if number is prime number
    assign = True
    for i in range (2,int(sqrt(number))+1):
        if number % i == 0:
            assign = False
    return assign    

pri_list = [2,3]
i = 1
while len(pri_list) < 10001:
    if isprime(i*6-1): 
        pri_list.append(i*6-1)
    if isprime(i*6+1): 
        pri_list.append(i*6+1)
    i += 1
print(len(pri_list), 'th prime number is ', pri_list[-1])


## 3rd aproach (takes about 2 seconds): Using just sqrt from math module and own writen isprime function: Takes about 2 sec. Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of smaller factor that has been already checked.
#
#def isprime(number):
#    from math import sqrt
#    # returns true if number is prime number
#    assign = True
#    for i in range (2,int(sqrt(number))+1):
#        if number % i == 0:
#            assign = False
#    return assign    
#goal = 10001 # trying to find goal'th prime number
#i = j = 0
#while i <= goal:
#    j += 1
#    if isprime(j):
#        i += 1
#
#print(i, 'th prime number is ', j)


## 4th approach: Naive brute force, using self written isprime function. It takes about 2 minutes to compute. That's why kept it at 100th for now.
#def isprime(number):
#    # returns true if number is prime number
#    assign = True
#    for i in range (2,number):
#        if number % i == 0:
#            assign = False
#    return assign    
#
#goal = 100 # trying to find goal'th prime number
#i = j = 0
#while i <= goal:
#    j += 1
#    if isprime(j):
#        i += 1
#        print(i)
#
#print(i-1, 'th prime number is ', j)
