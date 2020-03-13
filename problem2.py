########################################################
# Problem 2 - Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the even-valued terms.
########################################################

import timer

n0, n1, s = 1, 2, 0
while n1 < 4000000:
    if n1%2 == 0:
        s += n1
    n1 = n1 + n0
    n0 = n1 - n0

print(s)

print(timer.end())

# 4613732
# 0.000055 seconds