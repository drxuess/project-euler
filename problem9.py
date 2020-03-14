########################################################
# Problem 9 - Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
########################################################

from functools import reduce
import timer

for n in range(1, 20):
    for m in range(n + 1, 21):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if (a+b+c) == 1000:
            print(a*b*c)
            break

print(timer.end())

# 31875000
# 0.000181 seconds