'''
OOP
-Inheritance
    -Child classes inherit methods and attributes from parent class
- Polymorphism
    - "Many Forms"
    - Ability of an object to be different classes
    -Method Overriding
        -Changing behavior of a method inherited from a parent class
    -Method Overloading 
        -Method polymorphism 
-Encapsulation
    - Having control over your attributes/ data members
    - Achieve encapsulation by making attributes private
        -*** CANT MAKE ATTRIBUTED PRIVATE IN PYTHON **
        -"Emulate" by prefixing attributes with _
    -Access attributes with control using setter/getter methods
-Abstraction
    -Handling complexity by hiding unnecessary information from the user
    -Achieved by using abstract classes
        -Class that has one or more abstract methods
            -Abstract method => unimplemented method
    -abc (Abstract Base Class) module used to create abstract classes
    

'''
from abc import ABC, abstractmethod
class Animal2(ABC):
    def __init__(self, name, age, color=""):
        self._name = str(name) #initializing attirbutes   #str type safety raising inception?
        self._age = int(age)
        self._color = str(color) # allow's us to save each object
       # if age < 0:
            #self.age = 0

    def setName(self, name):
        self._name = str(name)
    
    def getName(self):
        return self._name

    @abstractmethod
    def sleep(self):
        pass
   
    #def sleep(self):
       # print("***zzz***")
       

    def getOlder(self, years=1):
        self._age += years 

    @abstractmethod
    def move(self):
       # print("*", self.name, "has moved. *")
       pass
#overriding the string default method 
    
    def __str__(self):
        return "Name:" + self._name + ", Age: " + str(self._age) + ", Color: " + self._color

class Dog2(Animal2): #polymorphism of the dog class
    def sleep(self):
        print("***snore***")

    def move(self):
        print("*", self._name, "ran. *")

class Cat2(Animal2):
    def sleep(self):
        print("***PURR***")
    def move(self):
        print("*", self._name, "walked. *" )

class Horse2(Animal2):
    def sleep(self):
        print("***sleep***")
    
    def move(self):
        print("*", self._name, "galloped *")

    def feed(self):
        print("** Fed", self._name, "a carrot. **")

    
