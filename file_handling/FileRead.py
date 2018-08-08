f = open("test.txt",mode = 'r',encoding = 'utf-8')
print(f.read())
print()
print('Current position of cursor', f.tell())
print('Set cursor at 0 position : ', f.seek(0))


f = open("test.txt",mode = 'r',encoding = 'utf-8')
print(f.readline(), end = '')
print(f.readline(), end = '')
print(f.readline(), end = '')
print(f.readline(), end = '')
