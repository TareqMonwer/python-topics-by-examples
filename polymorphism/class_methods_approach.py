from typing import Any


class Dog:
    def sound(self):
        return "Bark"


class Cat:
    def sound(self):
        return "Meow"


# Function that takes an object and calls its sound method
def make_sound(animal: Any):
    print(animal.sound())


# Using polymorphism
dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Bark
make_sound(cat)  # Output: Meow
