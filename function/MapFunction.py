def double(x):
    return x * 2
    
l1 = [20, 10, 5, 6, 7, 32, 25, 16]
l2 = list(map(double, l1))
print(l2)

# l1 = [20, 30, 5, 6, 7, 32, 25, 16]
# l2 = [1, 2, 3, 4, 5]
# l3 = list(map(lambda x, y: x * y, l1, l2))
# print(l3)
