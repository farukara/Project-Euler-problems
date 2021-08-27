#!python3
# coding: utf-8
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
#https://projecteuler.net/problem=43

from itertools import permutations
from time import perf_counter

def timeit(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.4f} seconds")
        return value
    return wrapper

@timeit
def method1(): #1.7 seconds
    divisors = [2,3,5,7,11,13,17]
    combs = permutations(map(str, [x for x in range(10)]))
    total = 0
    for comb in combs:
        if comb[0] == "0":
            continue
        if int("".join(comb[7:10])) % 17 == 0 and \
                int("".join(comb[6:9])) % 13 == 0 and \
                int("".join(comb[5:8])) % 11 == 0 and \
                int("".join(comb[3:6])) % 5 == 0 and \
                int("".join(comb[4:7])) % 7 == 0 and \
                int("".join(comb[2:5])) % 3 == 0 and \
                int("".join(comb[1:4])) % 2 == 0:
                    total += int("".join(comb))

    print("Sum: ", total)

@timeit
def method2(): #0.0014 seconds
    def three_digit_list(higher_div_list, divisor):
        candidate_digits = []
        if not higher_div_list:
            i = 1
            while (prod := i*divisor) < 1000:
                if len(str(prod)) == len(set(str(prod))):
                    if len(str(prod)) < 3:
                        candidate_digits.append("0" + str(prod))
                    else:
                        candidate_digits.append(str(prod))
                i += 1
        else:
            for lower_digits in higher_div_list:
                available_numbers = [str(x) for x in range(10)]
                for digit in lower_digits:
                    #try:
                    available_numbers.remove(digit)
                    #except ValueError:
                    #    pass
                for one_digit in available_numbers:
                    if int(one_digit + lower_digits[:2]) % divisor == 0:
                        candidate_digits.append(one_digit + lower_digits)
        return candidate_digits
    
    divisors = [2,3,5,7,11,13,17]
    i = 0
    def recurcive(result, divisor):
        if divisor == 17:
            return three_digit_list(None, 17)
        else:
            return three_digit_list(result, divisors[i-1])
        return result
    print(recurcive(None, )
    result = None
    for divisor in divisors:
        recurcive(result, divisor)
    #digit_of_17 = three_digit_list(None, 17)
    #digit_of_13 = three_digit_list(digit_of_17, 13)
    #digit_of_11 = three_digit_list(digit_of_13, 11)
    #digit_of_7 = three_digit_list(digit_of_11, 7)
    #digit_of_5 = three_digit_list(digit_of_7, 5)
    #digit_of_3 = three_digit_list(digit_of_5, 3)
    #digit_of_2 = three_digit_list(digit_of_3, 2)
    for i in range(len(digit_of_2)):
        total = 0
        for j in digit_of_2[i]:
            total += int(j)
        remainder = 45 - total
        digit_of_2[i] = str(remainder) + digit_of_2[i]
    total = 0
    for number in digit_of_2:
        total += int(number)
    print("\nSum: ", total)

if __name__ == "__main__":
    method2()
