d = {'a':'Apple', 'b':'Ball'}
print(d)
d['c'] = 'Cat'
print(d)

print('\nContain : ',d.__contains__('a'))

d.__setitem__('e', 'Elephant')
print('\nAfter Adding: ', d)

d.__delitem__('e')
print('\nAfter Delete : ',d)

d.__setitem__('b', 'Baby')
print('\nSet new value: ',d)
