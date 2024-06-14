class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)
    
rect = Rectangle("Yellow", 5, 10)
print(rect.color)
print(rect.area())

circ = Circle("Pink", 7)
print(circ.color)
print(circ.area())
