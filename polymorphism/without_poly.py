class Dog:
    def bark(self):
        print("Woof!")


class Cat:
    def meow(self):
        print("Meow!")


def make_sound_dog(dog):
    dog.bark()


def make_sound_cat(cat):
    cat.meow()


# Using separate functions for each animal
dog = Dog()
cat = Cat()
make_sound_dog(dog)  # Output: Woof!
make_sound_cat(cat)  # Output: Meow!
