#! python3
# coding: utf-8
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,
# 349 + 943 = 1292,  
# 1292 + 2921 = 4213  
# 4213 + 3124 = 7337
# That is, 349 took three iterations to arrive at a palindrome.
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
# How many Lychrel numbers are there below ten-thousand?
# Note: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
# https://projecteuler.net/problem=55

from time import perf_counter

def timed(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{func.__name__}\" function took {finish - start:.2f} seconds")
        return value
    return wrapper

def is_palindrome(n):
    "returns True if n is a palindrome"
    for i in range(len(str((n)//2))):
        if int(str(n)[i]) != int(str(n)[-1-i]):
            return False
    return True

def is_lychrels(n):
    "returns True if n can not produce a palindrome \
    by reverse and add method in 50 iterations"
    for i in range(50):
        reverse = int(str(n)[::-1])
        n = n+reverse
        if is_palindrome(n):
            return False
    return True

@timed
def main():
    num_of_lychrels = 0
    for i in range(10_000):
        if is_lychrels(i):
            num_of_lychrels += 1
    print("\n", num_of_lychrels)

if __name__ == "__main__":
    main()
