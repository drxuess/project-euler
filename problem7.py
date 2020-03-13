########################################################
# Problem 7 - 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, 
# and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
########################################################

import math
import timer

primes = [2, 3, 5, 7, 11, 13]

def isPrime(n):
    for x in primes:
        if n%x == 0:
            return False
    x = primes[len(primes)-1]
    while x <= math.sqrt(n):
        if n%x == 0:
            return False
        x += 1
    primes.append(n)
    return True

n = 18 #6*3
while len(primes) <= 10000:
    isPrime(n-1)
    isPrime(n+1)
    n += 6


print(primes[len(primes)-1])

print(timer.end())

# 104743
# 1.868716 seconds