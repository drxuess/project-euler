########################################################
# Problem 4 - Largest palindrome product
#
# A palindromic number reads the same both ways. The largest 
# palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of 
# two 3-digit numbers.
########################################################

import timer

products = [x * y for x in range(100, 1000) for y in range(100, 1000)]
products.sort(reverse=True)

for n in products:
    nList = list(str(n))
    if nList == nList[::-1]:
        print(n)
        break

print(timer.end())

# 906609
# 0.152987 seconds