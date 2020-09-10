##! Python3
## By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
## https://projecteuler.net/problem=2 


# TODO First approach: Naive recursive approach with exponential time. README for more info
# TODO Second approach: Memoization

#Third approach: Bottom-up aproach (still using memoization at its core)
fib = [1, 2] #initial fibonacci list
total = 2 #initital total of evens

while fib[-1] < 4_000_000: #minus 2 because we already assigned first 2
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
        total += fib[-1]
    del fib[0] #always deleting first item to save memory. TODO This is actually costfull because of calling a function. Using a list of length 2 would be faster.

print(total)
