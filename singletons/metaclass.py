from typing import Any


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(
                *args, **kwds
            )
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)
