l = [[10,20,30],[40,50,60],[70,80,90]]
print('List Elements : ', l)

print('\nRow Elements : ')
for x in l:
    print(x)

print('\nMatrix Elements: ', end='')
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=' ')
    
print()