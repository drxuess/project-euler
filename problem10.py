########################################################
# Problem 10 - Summation of prime
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
########################################################

import timer

x = 2000000

numbers = set(range(x, 1, -1)) #generate list of numbers from 2 -> x
primes = []
while numbers:
    n = numbers.pop() #take the smallest number
    primes.append(n) #add it to the primes list
    numbers.difference_update(set(range(n*2, x+1, n))) #remove all multiples of this number and repeat(*2 because all primes are odd)

print(sum(primes))
print(timer.end())

# 142913828922
# 0.518388 seconds