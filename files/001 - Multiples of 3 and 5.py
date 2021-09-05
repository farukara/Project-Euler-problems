##! Python3
## Find the sum of all the multiples of 3 or 5 below 1000. 
## https://projecteuler.net/problem=1 


#total = 0
#for i in range(1000):
#	if i%3 == 0 or i%5 == 0:
#		total += i
#print(total)
#    		
#                
#a better, cleaner code:
    
total = sum(i for i in range(1000) if i%3 == 0 or i%5 == 0)
print(total)

