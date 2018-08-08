class Student(object):

    def __init__(self, name, ph):
        self.name = name
        self.ph = ph
        
    def display(self):
        print('Name of student : ', self.name)
        print('Phone number : ', self.ph)
        

s = Student('Ashwin', 9874563210)
s.display()
print(s.__dict__)