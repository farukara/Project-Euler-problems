#! Python3
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
# https://projecteuler.net/problem=20

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum

if __name__ == "__main__":
    n = 100
    print(factorial(n))
    print(sum_of_digits(factorial(n)))

