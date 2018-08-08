class Point(object):    
    shape = 'Circle'  # Static variables
    
    def __init__(self):
        print('\nInside constructor : ')    
        print('Using self : ', self.shape)
        print('Using class name : ', Point.shape)

    @staticmethod  
    def define():
        print('\nInside static method : ') 
        print('Using class name : ', Point.shape)
    
    @classmethod
    def define2(cls):
        print('\nInside class method : ') 
        print('Using cls : ', cls.shape)
        print('Using class name : ', Point.shape)
    
    def display(self): 
        print('\nInside instance method : ')        
        print('Using self : ', self.shape)
        print('Using class name : ', Point.shape)
        
p = Point()
p.display()
Point.define()
p.define2()
