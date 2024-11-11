# Define a metaclass to enforce the structure
class ModelMeta(type):
    def __init__(cls, name, bases, dct):
        if cls.__name__ != "BaseModel":
            # Check if 'fields' attribute is defined
            if not hasattr(cls, "fields") or not isinstance(cls.fields, list):
                raise TypeError(
                    f"Class {name} must define a 'fields' attribute as a list."
                )

            # Check if 'save' method is implemented
            if "save" not in dct or not callable(dct["save"]):
                raise TypeError(
                    f"Class {name} must implement a 'save()' method."
                )

            # Call the parent __init__ method
            super().__init__(name, bases, dct)


# Using the metaclass for model classes
class BaseModel(metaclass=ModelMeta):
    pass


# A valid model class
class UserModel(BaseModel):
    fields = ["username", "email"]

    def save(self):
        print("Saving UserModel data...")


# An invalid model class (will raise a TypeError)
class InvalidModel(BaseModel):
    # Missing 'fields' and 'save' method
    pass
