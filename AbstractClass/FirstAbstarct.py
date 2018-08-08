from abc import ABC, abstractmethod


class Test (ABC):

    @abstractmethod
    def addition(self):
        ''' data '''


class Demo(Test):
    
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def addition(self):
        return self.a + self.b

    
t = Demo(10, 20)
print(t.addition())
