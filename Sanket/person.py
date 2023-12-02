from abc import  ABC,abstractmethod

#prototype
class Person(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def display(self):
        pass
    
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
        
# method used
# abstractmethod
# clone=Make exact copy of orignal code
# display=display the name
# get method= return the value of variable name
# set method= assign a value to name variable
# abc=we can not create abstract class directly in python so we use module abc that 
# provide the infrastructure for defining the base of abstract base class
    
        
    
    
    