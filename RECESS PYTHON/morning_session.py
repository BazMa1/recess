#INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
        
        #method overriding
class dog(Animal):
    def barking(self):
        print(self.name,"is barking")
        
class cat(Animal):
    def meowing(self):
        print(self.name, "is Meowing")
        
#create objects
#animal1 = Animal()
dog1= dog("ken")
cat1 = cat("ben")
#call the objects
dog1.barking()
cat1.meowing()
print("==============================================================================")

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  
print("========================================================================================================")

#EXERCISE

class Shape:
    def __init__(self, radius):
        self.radius = radius
    


class Circle(Shape):
    def __init__(self, radius):
      super().__init__(radius)

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14* self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# method
circle = Circle(5)
print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())
print('==============================================')


#example
class Animal2:
    def __init__(self,name):
        self.name =name
        print('Animal created')

    def eat(self):
        print(self.name,"is eating")       
        
class Fly:
    def __init__(self,name):
        self.name= name
        print(self.name ,'is ready to fly!')
        
        
#create class that inheritances
class Bird(Animal,Fly):
    #constructor
    def __init__(self,name,type):
        self.type= type
        super().__init__(name)
    def sing(self):
        print(self.name,'sings a song and is type of ',self.type)
#bird =Bird('Parrot')
#create type
myanimal = Animal2("dog")
myanimal.eat()
mybird =Bird("hen",'poultry')
#mybird.eat()
mybird.sing()
print('======================================')


#POLYMORPHISM
class Shape:
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self ,radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius **2


class Rectangle(Shape):
    def __init__(self ,length,width):
        self.length =length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
#create objects
mycircle = Circle(5)
myrectangle = Rectangle(5,10)

#display result
print('rectangle area',myrectangle.calculate_area())
print('circle area',mycircle.calculate_area())
#print("===================OVER RIDING==========================================")
              
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphism in action
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()
#print('===============METHOD OVERLOADING=====================')
"""_summary_
class MathUtils:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math = MathUtils()
print(math.add(2, 3))        # Calls the first add method
print(math.add(2, 3, 4))     # Calls the second add method

        """
print('===========ABSTRACTION==================')
from abc import ABC

class Shape(ABC):
    #@abstractmethod
    def area(self):
        pass

    #@abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


#create rectangle results
rectangle = Rectangle(5, 3)


#display rectangle results
print('rectangle area:',rectangle.area())      # Output: 15
print('rectangle perimter:',rectangle.perimeter()) # Output: 16


class Circle(Shape):
    def __init__(self ,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius**2
    def perimeter(self):
        return  2*3.14*self.radius
    
    
#create circle object
circle = Circle(2)


#display circle results
print('circle area:',circle.area())
print('circle perimeter:',circle.perimeter())
