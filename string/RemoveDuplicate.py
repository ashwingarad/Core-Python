s = input('Enter String : ')
s1 = ''
i = 0
n = len(s)
while n > i :
    if s[i] not in s1:
        s1 += s[i]
    i += 1

print(s1) 
