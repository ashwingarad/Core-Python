s = input('Enter String : ')
s1 = s2 = output = ''
for x in s:
    if x.isalpha() :
        s1 += x
    else:
        s2 += x;

for x in sorted(s1):
    output += x
    
for x in sorted(s2):
    output += x
    
print('Result: ', output)
