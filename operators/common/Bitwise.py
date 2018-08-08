'''
Created on 24-Apr-2018

@author: Ashwin
'''
x = 10          #0000 1010
y = 4           #0000 0100
print(x | y)    # 14 (0000 1110)
print(~x)       # -11 (1111 0101)
print(x ^ y)    # 14 (0000 1110)
print(x >> 2)   # 2 (0000 0010) 
print(x << 2)   # 40 (0010 1000)

x=-20
print(x>>2)