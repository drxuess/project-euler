########################################################
# Problem 5 - Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
########################################################

import timer

def divisibleBy(number):
    for div in range(20, 0, -1):
        if number%div != 0:
            return False
    return True

n = 20
while not divisibleBy(n):
    n += 20

print(n)

print(timer.end())

# 232792560
# 3.499385 seconds