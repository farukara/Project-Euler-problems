#! Python3
## Find the largest palindrome made from the product of two 3-digit numbers.
## https://projecteuler.net/problem=4

from time import perf_counter

def polindrome_product_finder(digits):
    upper_limit = int('1' + number_of_digits * '0')
    lower_limit = int('1' + (number_of_digits-1) * '0')

    m = upper_limit
    palindromes = []
    while m > lower_limit:
        n = upper_limit
        while n > lower_limit:
            prod = m*n
            if int(str(prod)[:int(len(str(prod))/2)])== int(str(prod)[::-1][:int(len(str(prod))/2)]):
                palindromes.append(prod)
            n -= 1
    
        m -= 1
    print(max(palindromes))
    
if __name__ == '__main__':
    number_of_digits = 3  # this line is to avoid hard coding
    start = perf_counter()
    polindrome_product_finder(number_of_digits)
    print(perf_counter() - start)
