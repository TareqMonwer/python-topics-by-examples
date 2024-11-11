class Engine:
    def __init__(self) -> None:
        self.state = 'off'

    def start(self):
        print("Engine starting...")
        self.state = "running"


class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine

    def start(self):
        self.engine.start()  # Delegate the start behavior to the Engine


# Using composition
car = Car()
car.start()  # Output: Engine starting...
