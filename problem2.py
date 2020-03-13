n0, n1, s = 1, 2, 0
while n1 < 4000000:
    if n1%2 == 0:
        s += n1
    n1 = n1 + n0
    n0 = n1 - n0
print(s)