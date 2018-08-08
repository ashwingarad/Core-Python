s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print('First Set : ', s1)
print('Second Set : ', s2)

print('\nUnion : ', s1.union(s2))
print('s1 | s2 : ', s1 | s2)

print('\nDifference : ', s1.difference(s2))
print('s1 - s2 : ', s1 - s2)

print('\nSymmetric_difference : ', s1.symmetric_difference(s2))
print('s1 ^ s2 : ', s1 ^ s2)

print('\ns1 is subset s2 : ', s1.issubset(s2))
print('s1 <= s2 : ', s1 <= s2)

print('\ns1 is superset s2 : ', s1.issuperset(s2))
print('s1 >= s2 : ', s1 >= s2)