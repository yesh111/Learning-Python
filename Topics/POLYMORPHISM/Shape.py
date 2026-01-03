class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area of Circle: {3.14 * self.radius * self.radius}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"Area of Rectangle: {self.length * self.width}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"Area of Square: {self.side * self.side}"

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Square(3)
]

for shape in shapes:
    print(shape.area())
