from typing import Any, List, Literal


class Animal:
    def make_sound(self) -> Any:
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def make_sound(self) -> Literal['Bark']:
        return "Bark"


class Cat(Animal):
    def make_sound(self) -> Literal['Meow']:
        return "Meow"


# Polymorphism in action
animals: List[Any] = [Dog(), Cat()]

for animal in animals:
    # make_sound function works for any Animal type and behaves differently.
    print(animal.make_sound())
# Output:
# Bark
# Meow
