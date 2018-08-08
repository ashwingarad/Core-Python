'''
Created on 27-Apr-2018

@author: Ashwin
'''
import sys

list = [1, 2, 3, 4]
it = iter(list) 
print (next(it))

for x in it:
    print (x, end=" ")
    
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()