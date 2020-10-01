#! Python3
## Find the largest palindrome made from the product of two 3-digit numbers.
## https://projecteuler.net/problem=4

def polindrome_product_finder(digits):
    upper_limit = number_of_digits * 333
    lower_limit = number_of_digits * 33
    pairs_found = False

    m = upper_limit
    while m > lower_limit and pairs_found == False:
        n = upper_limit

        while n > lower_limit:
            prod = m*n
            if len(str(prod))%2 == 0:
                if int(str(prod)[:int(len(str(prod))/2)])== int(str(prod)[::-1][:int(len(str(prod))/2)]):
                    pairs_found = True
                    break
                    
            n -= 1
    
        m -= 1
    
    print(m+1, n)

if __name__ == '__main__':
    number_of_digits = 3  # this line is to avoid hard coding, can accept user input
    polindrome_product_finder(number_of_digits)
