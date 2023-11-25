# Переписать код в соответствии с Liskov Substitution Principle:


class Rectangle:
    def init(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.width = height
        self.height = height
