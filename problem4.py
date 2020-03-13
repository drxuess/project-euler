products = [x * y for x in range(100, 1000) for y in range(100, 1000)]
products.sort(reverse=True)

for n in products:
    nList = list(str(n))
    if nList == nList[::-1]:
        print(n)
        break