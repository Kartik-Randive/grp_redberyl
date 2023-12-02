import copy
from person import Person
from teacher import Teacher

#concreateprototype2

class Student(Person):
    def __init__(self, name, teacher):
        super().__init__(name)
        self.teacher=teacher
  
def clone(self):
    return copy.copy(self)

def display(self):
    print("Student Was Cloned")
    print(f'Student Name:{self.name}')
    print(f'Taught by:{self.teacher.get_name()}')
    
def get_teacher(self):
        return self.teacher
    
def set_teacher(self,teacher):
        self.teacher=teacher 
