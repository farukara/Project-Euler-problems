#! Python3
## finds largest prime factor of a given number
## https://projecteuler.net/problem=3

from time import perf_counter

def find_largest_prime_factor(n):
    """find largest prime factor of n"""
    def isprime(number):
        from math import sqrt
        # returns true if number is prime number
        if number % 2 == 0:
            return False
        for i in range (3, int(sqrt(number))+1, 2):
            if number % i == 0:
                return False
        return True

    if isprime(n):
        print(n, "is already a prime number, don't have any factors")
        return None
    else:
        for i in range(3, n//2+1, 2): #this eleminates powers of 2
            if (n/i)%1 == 0:
                if isprime(int(n/i)):
                    break

    return(int(n/i))


if __name__ == "__main__":
    n = 600851475143
    start = perf_counter()
    print('largest prime factor of ', n, 'is : ', find_largest_prime_factor(n))
    print('Time: ', perf_counter() - start)

