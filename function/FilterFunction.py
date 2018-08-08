def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

        
l = [20, 15, 67, 24, 32, 48, 41]
l1 = list(filter(isEven, l))
print(l1)


# l1 = [20, 15, 67, 24, 32, 48, 41]
# l2 = list(filter(lambda x : True if x%2 == 0 else False, l1))
# print(l1)
