from behaviors.swims import Swims
from behaviors.walks import Walks


class Duck:
    def __init__(self) -> None:
        self.swimmable = Swims()
        self.walkable = Walks()

    def perform_walk(self):
        self.walkable.walk()

    def perform_swim(self):
        self.swimmable.swim()


if __name__ == '__main__':
    duck = Duck()
