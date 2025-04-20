import copy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle(radius={self.radius})"