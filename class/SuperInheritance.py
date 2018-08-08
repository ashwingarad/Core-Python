class Base(object):
 
    def __init__(self, x):
        self.x = x    

 
class Derived(Base):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
 
    def display(self):
        # Note that Base.x won't work here
        # because super() is used in constructor
        print(self.x, self.y)


# Driver Code
d = Derived(10, 20)
d.display()
