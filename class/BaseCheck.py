class Base(object):
    pass   # Empty Class
 
class Derived(Base):
    pass   # Empty Class
 
# Driver Code
print("'Derived' class is sub class of 'Base' : ",issubclass(Derived, Base))
print("'Base' class is sub class of 'Derived' : ",issubclass(Base, Derived))
 
d = Derived()
b = Base()
 
# b is not an instance of Derived
print("'b' is instance of 'Derived' : ",isinstance(b, Derived))
 
# But d is an instance of Base
print("'d' is instance of 'Base' : ",isinstance(d, Base))
