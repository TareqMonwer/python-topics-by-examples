class Base:
    def action(self):
        print("Action from Base")


class A(Base):
    def action(self):
        super().action()
        print("Action from A")


class B(Base):
    def action(self):
        print("Action from B")


class Multiple(A, B):
    pass


print(Multiple.__mro__)
m = Multiple()
m.action()
