
fib = [1, 2] #initial fibonacci list
total = 2 #initital total of evens

while fib[-1] < 4_000_000: #minus 2 because we already assign first 2
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
        total += fib[-1]
    del fib[0] #always deleting first item to save memory

print(total)
