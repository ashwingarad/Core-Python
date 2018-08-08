s = input('Enter String : ')
i = 0
s1 = '' 
while len(s) > i :
    if s[i] not in s1:
        s1 += s[i]
    i += 1

i = 0 
while len(s1) > i:    
    print(s1[i], ':', s.count(s1[i]))
    i += 1