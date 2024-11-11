from behaviors.swims import Swims
from behaviors.walks import Walks


class Duck(Walks, Swims):
    pass


if __name__ == '__main__':
    duck = Duck()
    
    # using inheritance
    # duck.swim()  # swmming from swimmable
    # duck.walk() # walking from walkable
