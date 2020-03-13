import math

def largestPrime(n):
    for x in range(2, int(math.sqrt(n))):
        if n % x == 0 and not n/x == 1:
            n = largestPrime(n / x)
    return n

print(largestPrime(600851475143))