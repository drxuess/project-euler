########################################################
# Problem 6 - Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
#
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
#
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.
########################################################

from functools import reduce
import timer

sumOfSquares = reduce(lambda x , y: x + y**2, range(1, 101))
squareOfSum = reduce(lambda x , y: x + y, range(1, 101))**2

print(squareOfSum - sumOfSquares)

print(timer.end())

# 25164150
# 0.000049 seconds