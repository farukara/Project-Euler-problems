#! Python3
# finds largest prime factor of a given number

def find_largest_prime_factor(n):
    # find largest prime factor of n
    def isprime(number):
        # returns true if number is prime number
        assign = True
        for i in range (2,number):
            if number % i == 0:
                assign = False
        return assign    


    if isprime(n):
        print(n, "is already a prime number, don't have any factors")

    for i in range(2, round(n/2+1)):
        if (n/i)%1 == 0:
            if isprime(int(n/i)):
                break

    return(int(n/i))


    

if __name__ == "__main__":
    n = 13195
    print('largest prime factor of ', n, 'is : ', find_largest_prime_factor(n))
