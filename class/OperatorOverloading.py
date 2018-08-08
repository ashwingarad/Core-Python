class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return 'Addition of 2 objects is {} and {}' .format(self.a, self.b)
        
    def __add__(self, other):
        return Calc(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Calc(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        return Calc(self.a * other.a, self.b * other.b)
    
    def __mod__(self, other):
        return Calc(self.a % other.a, self.b % other.b)
    
    def __floordiv__ (self, other):
        return Calc(self.a // other.a, self.b // other.b)
    
    
c1 = Calc(10, 20)
c2 = Calc(15, 45)
print(c1 + c2)
