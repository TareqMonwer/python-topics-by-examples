# Define a custom metaclass
from typing import Any


class MyMeta(type):
    def __new__(cls, name: str, bases: str, dct: dict[str, Any]):
        # Modify the class attributes before the class is created
        # dct["greet"] = lambda self: print(f"Hello from {name}!")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        # Perform initialization tasks
        print(f"Initializing class {name}")
        print(f"Bases: {bases}")
        print(f"Attributes: {dct}")

        # You can perform additional setup or validation here
        if "greet" not in dct:
            raise TypeError(f"{name} must have a 'greet' method")

        # Call the parent __init__ method
        super().__init__(name, bases, dct)


# Use the custom metaclass
class MyClass(metaclass=MyMeta):
    pass


# Create an instance of MyClass
obj = MyClass()
# obj.greet()
