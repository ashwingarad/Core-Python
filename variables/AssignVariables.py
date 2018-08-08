import sys
from builtins import input
from pip._vendor.distlib.compat import raw_input

counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "Hello Python"  # A string

print (counter)
print (miles)
print (name, '\n')

# Assignment
print('Multiple Assignment')
a = b = c = 1
print(a); print(b); print(c)

a, b, c = 10, 20.2, "Hello Python"  # re-declaring the variable
print()
print(a); print(b); print(c)

x = input("\nEnter Value : ")
print("Entered Value is : ", x)

x = raw_input("\nEnter String : ")  # entered data is treated as string even without ''
print("Enter input treated as String : ", x)

sys.exit(1)
