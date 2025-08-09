class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        area = NotImplementedError()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"The area of the Rectangle is: {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __str__(self):
        return f"The area of the Circle is: {self.area()}"