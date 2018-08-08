class Point(object):    
    shape = 'Circle'  # Static variables
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod  
    def define():
        print('It is only used to access')
    
    @classmethod
    def define2(cls):
        cls.shape = 'Triangle'
    
    def display(self):
        print('x : ', self.x , end='\t\t')
        print('y : ', self.y , end='\t\t')
        print('Shape : ', self.shape)  # Access static variable


print('Before Value change: ')
s1 = Point(10, 40)
s1.display()

s2 = Point(40, 20)
s2.display()

Point.shape = 'Square'  # Change the value of static variable
print('\nAfter Value change: ')
s1.display()
s2.display()

print('\nAfter calling static method : ')
Point.define2()
s1.display()
s2.display()
