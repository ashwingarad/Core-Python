class Parent:
    
    @staticmethod
    def a():
        print('Parent Static method ')
    
    @classmethod
    def b(cls):
        print('Parent Class method ')


class Sub(Parent):
    
    @staticmethod
    def a():
        print('Sub Static method ')
    
    @classmethod
    def b(cls):
        print('Sub Class method ')

        
Parent.a()
Parent.b()
Sub.a()
Sub.b()
print()
p = Parent()
s = Sub()
p.a()
p.b()
s.a()
s.b()