class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount


# OBJECT
employee = Employee("BAZZIWE MARVIS", 7500000)
print("Employee name:", employee.get_name())
print("Employee salary:", employee.get_salary())
#INCREASE
increment_amount = 1500000
employee.increment_salary(increment_amount)

print("New salary:", employee.get_salary())
