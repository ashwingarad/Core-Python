class Test:

    def __init__(self, a, b):
        print('Constructor initialized')
        self.a = a
        self.b = b
        
    def display(self):
        total = self.a + self.b  # total is local variable
        print('Sum ', total)
        
        
t = Test(10, 20)
t.display()
