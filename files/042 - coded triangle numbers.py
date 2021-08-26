#!python3
# coding: utf-8
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
#https://projecteuler.net/problem=42

from time import perf_counter

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start:.3f} seconds")
        return result
    return wrapper

@timeit
def main():
    triangle_num_values = []
    for i in range(1, 27):
        triangle_num_values.append(int(i*(i+1)*0.5))

    counter = 0
    with open("p042_words.txt", "r") as f:
        words = f.readlines()[0][1:-1].split('","')
        for word in words:
            sum_of_letters = 0
            for letter in word:
                sum_of_letters += ord(letter)-64
            if sum_of_letters in triangle_num_values:
                counter += 1

    print("\n", counter)

if __name__ == "__main__":
    main()
