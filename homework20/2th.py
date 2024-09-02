"""Write an abstract class with name GeometricFigure
Write 2 geometric figure classes by inheriting from GeometricFigure
Write 2 functions
get_perimeter -> return perimeter of figure
get_area -> return area of figure"""


from abc import ABC, abstractmethod
class GeometricFigure(ABC):
    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Square(GeometricFigure):
    def __init__(self, side):
        self.side = side
    def get_perimetr(self):
        return self.side * 4
    def get_area(self):
        return self.side ** 2

class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimetr(self):
        return (self.width + self.height) * 2
    def get_area(self):
        return self.width * self.height

square = Square(5)
rectangle = Rectangle(4, 5)
print(square.get_perimetr())
print(square.get_area())
print(rectangle.get_perimetr())
print(rectangle.get_area())
