class Shape:
    def __init__(self, name):
        self.name = name
    
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rect = Rectangle("Rectangle1", 5, 10)

print(f"Shape Name: {rect.name}")
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")
print(f"Area: {rect.calculate_area()}")

print(f"Is rect a Shape? {'Yes' if isinstance(rect, Shape) else 'No'}")
print(f"Is rect a Rectangle? {'Yes' if isinstance(rect, Rectangle) else 'No'}")