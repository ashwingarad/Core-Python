l = []
for x in range(1,20):
    l.append(x)

print('list : ',l)

b = bytes(l)
for x in range(len(b)):
    print(b[x], end=' ')
