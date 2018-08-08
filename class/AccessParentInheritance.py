class Base(object):
 
    def __init__(self, x):
        self.x = x    

 
class Derived(Base):
 
    def __init__(self, x, y):
        Base.x = x 
        self.y = y
 
    def display(self):
        print('Base class value : ', Base.x)
        print('Derived class value : ', self.y)
 
 
# Driver Code
d = Derived(10, 20)
d.display()
