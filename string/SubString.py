s1 = input('Enter 1st String : ')
s2 = input('Enter 2nd String : ')

flag = False
pos = -1

while True:
    pos = s1.find(s2, pos + 1, len(s1))
    if pos == -1:
        break
    else:
        flag = True
        print('String found at : ', pos ,' Position')

if flag == False:
    print('Sub String not found')
