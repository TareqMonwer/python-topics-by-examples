from behaviors.flyable import Flyable
from behaviors.swims import Swims
from behaviors.walks import Walks


class HomoSapience(Walks, Flyable, Swims):
    pass
