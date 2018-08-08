no = int(input('How many Students you have to enter : '))
d1 = {}
for x in range(no):
    name = input('\nEnter {} Name of Student : '.format(x + 1))
    mark = input('Enter {} marks of student : '.format(x + 1))
    
    d1[name] = mark
    
print('\n', d1)

while True:
    name = input('\nEnter name of student to find marks : ')
    mark = d1.get(name, -1)
    if mark == -1:
        print('Student not found')
    else:
        print('The marks of {} is {}'.format(name, mark))
    
    opt = input('\nDo you want to find another student mark [Y/N]: ')
    if opt == 'N' or opt == 'n':
        break