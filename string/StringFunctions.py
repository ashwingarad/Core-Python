s = '***Python \t Programming \t Language***'
print('\n String : ' , s)
print('\n Replace "a" with "b" : ', s.replace('a', 'b'))
print('\n count "m" : ', s.count('m'))
print('\n split : ', s.split())
print('\n rsplit "a" :> ', s.rsplit('a'))
print('\n lstrip "*" :> ', s.lstrip('*'))
print('\n strip "*" :> ', s.strip('*'))
print('\n lower : ', s.lower())
print('\n upper : ', s.upper())
print('\n swapcase : ', s.swapcase())
print('\n endswith "*" : ', s.endswith('*'))
print('\n center : ', s.center(47, '$'))
print('\n ljust : ', s.ljust(47))

t = ('Python', 'Java', 'Android', 'Spring')
print('\n\n Tuple : ', t)
print('\n join "#" : ', ' # '.join(t))

l = 'commerce science commerce'
print('\n\n String : ', l)
print('\n capitalize : ', l.capitalize())
print('\n title : ', l.title())

n = 'Python3'
print('\n\n String : ', n)
print('\n isalnum : ', n.isalnum())

m = 'Python'
print('\n\n String : ', m)
print('\n isalpha : ', m.isalpha())

intab = "aeiou"
outtab = "12345"
trans = m.maketrans(intab, outtab)
print('\n maketrans : ', trans)
print('\n translate : ', s.translate(trans))
