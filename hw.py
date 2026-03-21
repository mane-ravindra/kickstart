#!/usr/bin/python
print("Hello World!")

a = 12
b = 13.5

print(a+b)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
s1 = Student("Ravi", 20)

# Calling method
# s1.display()