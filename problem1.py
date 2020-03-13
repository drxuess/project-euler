from functools import reduce
sum3 = reduce(lambda x, y: x + y, range(3, 1000, 3))
sum5 = reduce(lambda x, y: x + y, range(5, 1000, 5))
sum35 = reduce(lambda x, y: x + y, range(15, 1000, 15))
print(sum3 + sum5 - sum35)