class Point(object):
    shape = 'Circle'  # Static variables
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
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
