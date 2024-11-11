class ActionClasses(type):
    def __new__(cls, name, bases, dct: dict[str, str]):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith('do'):
                raise TypeError('Method names must start with "do"')

        return super().__new__(cls, name, bases, dct)


class BaseAction(metaclass=ActionClasses):
    def do(self):
        pass


class ScrollAction(BaseAction):
    def do_scroll(self):
        pass


class NoAction(BaseAction):
    def nothing(self):
        pass
