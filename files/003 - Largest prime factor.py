
def isprime(number):
    assign = True
    for i in range (2,number):
        if number % i == 0:
            assign = False
    return assign    

for i in range(50):
    print(i, ':', isprime(i))
