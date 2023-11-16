# Mahdi Mohammadi khah 982011056

class Person:
    def __init__(self, name, email):
       self.name = name
       self.email = email

    @staticmethod
    def get_age(age):
        print(age)


class Employee(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'employee'

    @staticmethod
    def get_age():
        print(50)


name = input()
email = input()
employee = Employee(name, email)
print(employee.name)
print(employee.email)
employee.get_age()