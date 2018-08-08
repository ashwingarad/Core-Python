s = input('Enter String : ')
s1 = s2 = result = ''

for x in s:
    if x.isalpha():
        s1 += x 
    elif x.isdigit():
        s2 += x

print('Alphabet : ', s1)
print('Digit : ', s2)

for x in sorted(s1):
    result += x
    
for x in sorted(s2):
    result += x
    
print('Sorted order : ', result)
