# Mahdi Mohammadi khah 982011056

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age


class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.role = 'employee'


name = input()
age = input()
employee = Employee(name, age)
print(employee.name)
print(employee.age)