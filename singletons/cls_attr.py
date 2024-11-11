from typing import Self


class ClassAttrBasedSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(ClassAttrBasedSingleton, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance


s1 = ClassAttrBasedSingleton()
s2 = ClassAttrBasedSingleton()

print(s1 is s2)