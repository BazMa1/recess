class Student:
    def __init__(self, name,year,course):
        self.name = name
        self.year= year
        self.course = course
        
    def display_student(self):
        print("Name:",self.name)
        print("Year:",self.year)
        print("course:",self.course)
my_student = Student("BAZZIWE",3,"BSSE")      
my_student.display_student() 
    
#CIRCLE
class Circle:
    #constructor
    def __init__ (self , radius ): 
        self.__radius = radius
    #calculate area
    def Area(self):
       print("AREA:",3.14* self.__radius**2)
    #calculate circumference
    def Circumference(self):
        print("CIRCUM:",2*3.14*(self.__radius)**2)
#create method
my_circle = Circle(7)
my_circle.Area()
my_circle.Circumference()

#create bank account
#ENCAPSULATION USING UNDERSCORES
class BankAccount:
    def __init__(self,account_No,balance):
        self._account_no = account_No
        self._balance = balance
#deposit
    def deposit(self, amount):
         self._balance +=amount
#withdraw
    def withdraw(self, amount):
        if 0 < self._balance >= amount :
            self._balance -= amount
        else:
            raise ValueError('Insufficient funds')
    def get_balance(self):
           return self._balance
#create object
my_acc =BankAccount('5689',1000)
print(my_acc._account_no)
print(my_acc.get_balance())
my_acc.deposit(500)
print(my_acc.get_balance())
my_acc.withdraw(800)
print(my_acc.get_balance())


     
         
         
         