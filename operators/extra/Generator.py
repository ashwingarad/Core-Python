'''
Created on 27-Apr-2018

@author: Ashwin
'''
#!usr/bin/python3
import sys

def fibonacci(n):  # generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(5)  # f is iterator object

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit
