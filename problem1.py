########################################################
# Problem 1 - Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
########################################################

from functools import reduce
import timer

sum3 = reduce(lambda x, y: x + y, range(3, 1000, 3))
sum5 = reduce(lambda x, y: x + y, range(5, 1000, 5))
sum35 = reduce(lambda x, y: x + y, range(15, 1000, 15))

print(sum3 + sum5 - sum35)

print(timer.end())

# 233168
# 0.000074 seconds