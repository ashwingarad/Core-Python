from random import *
import time
for x in range(10):
    print('Randint ', randint(0, 10), end='\t')
    print('Randrange ', randrange(0, 10), end='\t')
    print('random ', random(), end='\t')
    seed(time.time())
    print('seed apply ', random())
