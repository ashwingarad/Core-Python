import functools
l1 = [20, 10, 5, 6, 7, 32, 25, 16]
l2 = functools.reduce(lambda x, y: x + y, l1)
print(l2)
