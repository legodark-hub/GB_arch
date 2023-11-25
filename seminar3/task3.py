# Переписать код в соответствии с Interface Segregation Principle:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass
    
class Circle(Shape):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

    def volume(self):
        raise NotImplementedError("Circle does not have volume")

class Cube(Shape):
    def init(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge