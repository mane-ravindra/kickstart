#!/usr/bin/python
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f"Hello, my name is {self.name} and I live in {self.city}.")