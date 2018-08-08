s = input('Enter String : ')
prev = ''
for x in s:        
    if x.isalpha():
        prev = x 
    elif x.isdigit():
        print(prev * int(x), end='')