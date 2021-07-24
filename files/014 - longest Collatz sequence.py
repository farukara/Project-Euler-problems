#! python3
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def seq_len(i):
    dictionary = {str(j): j for j in range(i+1)}
    max_len = 1
    while i > 1:
        if dictionary.get(str(i), False):
            seql = 0
            number = i
            while number != 1:
                if number%2 ==0:
                    number = number//2
                    try:
                        del(dictionary[str(number)])
                    except:# KeyError:
                        pass
                    seql += 1
                else:
                    number = number*3+1
                    try:
                        del(dictionary[str(number)])
                    except:# KeyError:
                        pass
                    seql += 1
            if seql > max_len:
                max_len = seql
                max_chain_number = i
        i -=1
    return max_chain_number, max_len

def seq_len_with_list(i):
    mask = [1]*(i+1)
    max_len = 1
    m = 1
    while m < i:
        if mask[m]:
            seql = 0
            number = m
            while number != 1:
                if number%2 ==0:
                    number = number//2
                    try:
                        mask[number] == 0
                    except:
                        pass
                    seql += 1
                else:
                    number = number*3+1
                    try:
                        mask[number] == 0
                    except:
                        pass
                    seql += 1
            if seql > max_len:
                max_len = seql
                max_chain_number = m
        m +=1
    return max_chain_number, max_len

def seq_len_with_memo(m):
    "dictionary with memoization"
    memo = {}
    i = 1
    dictionary = {str(j): j for j in range(m+1)}
    max_len = 1
    while i < m+1:
        if dictionary.get(str(i), False):
            seql = 0
            number = i
            while number != 1:
                if memo.get(str(number), False):
                    seql += memo[str(number)]
                    break
                if number%2 ==0:
                    number = number//2
                    try:
                        del(dictionary[str(number)])
                    except:# KeyError:
                        pass
                    seql += 1
                else:
                    number = number*3+1
                    try:
                        del(dictionary[str(number)])
                    except:# KeyError:
                        pass
                    seql += 1
            memo[str(i)] = seql
            #print(memo)
            if seql > max_len:
                max_len = seql
                max_chain_number = i
        i +=1
    return max_chain_number, max_len

if __name__ == "__main__":
    number = 1000000

    start = time.time()
    max_chain_number, max_len = seq_len_with_memo(number)
    print("Maximum sequence lenght is: ", max_len)
    print("Max Chain Number is: ", max_chain_number)
    end = time.time()
    print("Time: ", end - start, "\n")

    #start = time.time()
    #max_chain_number, max_len = seq_len(number)
    #print("Maximum sequence lenght is: ", max_len)
    #print("Max Chain Number is: ", max_chain_number)
    #end = time.time()
    #print("Time: ", end - start, "\n")

    #start = time.time()
    #max_chain_number, max_len = seq_len_with_list(number)
    #print("Maximum sequence lenght is: ", max_len)
    #print("Max Chain Number is: ", max_chain_number)
    #end = time.time()
    #print("Time: ", end - start)
