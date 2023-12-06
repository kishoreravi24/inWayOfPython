#!/usr/bin/python3
class Animal:
    def __init__(self,species):
        self.species = species
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Canine")
print(dog.species)
prit(dog.make_sound())

cat = Cat("Feline")
print(cat.species)
print(cat.make_sound())

