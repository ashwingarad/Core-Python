l = [
    x**2
    for x in range(1,20)
]

l2 = [
    x
    for x in l if x%2 == 0
]

print('First List : ',l)
print('Second Even Number List : ',l2)


words = ['Python', 'Java', 'CPP']
list3 = [ x[0]    for x in words ]

print(list3)


words = 'Python is very easy language than others'.split()

print('Words : ', words)

list4 = [
    [x.upper(),len(x)]
    for x in words
        
]

print(list4)