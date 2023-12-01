import copy
from person import Person

#concreateprototype1
class Teacher(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print("Teacher Was Cloned")
        print(f'Name:{self.name}')
        print(f'Who Teaches:{self.course}')
    
    def get_course(self):
        return self.course
    
    def set_course(self,course):
        self.course=course    
        
        
#super()= used to give access to methods and properties of parent class
#copy=made true copy of orignal ,copy.copy () make top level copy dosent copy nested object        
        