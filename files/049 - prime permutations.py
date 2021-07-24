#! python3
## The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this sequence?#! python3

def isprime(number):
    from math import sqrt
    # returns true if number is prime number
    controller = True
    for i in range (2,int(sqrt(number))+1):
        if number % i == 0:
            controller = False
    return controller    

i =1_000
while i<3_333:
    k = i+3330
    j = k+3330
    if all(map(isprime, (i,k,j))):
        control = True
        for number in str(i):
            if str(i).count(number) == str(j).count(number) and str(i).count(number) == str(k).count(number):
                pass
            else:
                control=False
                break
        if control:
            print(f"\nindividual numbers are: {i}, {k}, {j}")
            print(f'concatenated number is: {"".join(map(str,(i,k,j)))}')
    i += 1
