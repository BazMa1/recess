class Employee:
    def __init__(self, name,salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self,new_salary):
        self._salary = new_salary
    
    def increment_salary(self,increment_amount):
        self._salary += increment_amount
               
# CREATE OBJECT
my_emp = Employee("Bazz",8500000)
print("Employee name:",my_emp.get_name())
print("Employee salary:",my_emp.get_salary())

#INCREMENT salary
increment_amount = 1500000
my_emp.increment_salary(increment_amount)
print("NEW SALARY:",my_emp.get_salary())
        
