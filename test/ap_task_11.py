# Mahdi Mohammadi khah 982011056

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age


name = input()
age = input()

person = Person(name, age)
print(person.name)
print(person.age)