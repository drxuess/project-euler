########################################################
# Problem 3 - Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
########################################################

import math
import timer

def largestPrime(n):
    for x in range(2, int(math.sqrt(n))):
        if n % x == 0 and not n/x == 1:
            n = largestPrime(n / x)
    return n

print(largestPrime(600851475143))

print(timer.end())

# 6857.0
# 0.051796 seconds