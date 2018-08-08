s = input('Enter String : ')
u = 0
output = prev = ''
for x in s:
    if x.isalpha():
        prev = x
    elif x.isdigit():
        output += prev + chr(ord(prev) + int(x))  
        # ord ==> convert character to unicode
        # chr ==> convert unicode to character
print(output)
