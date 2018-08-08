import time
from imp import reload
import module1
print('Addition is: ', module1.add(10, 20))

print('Entering in sleeping state')
time.sleep(2)
reload(module1)
print('End of program')
