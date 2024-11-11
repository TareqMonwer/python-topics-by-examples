from typing import Any


def singleton(cls):  # type: ignore
    instances = {}

    def get_instance(*args, **kwargs) -> Any:  # type: ignore
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # type: ignore

    return get_instance  # type: ignore


@singleton
class SingletonClass:
    pass


# Usage
singleton1 = SingletonClass()
singleton2 = SingletonClass()

print(singleton1 is singleton2)
