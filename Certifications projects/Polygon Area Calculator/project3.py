import math

class Rectangle:
    def __init__(self, width, height):
        # Store width and height as instance attributes
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # Area = width × height
        return self.width * self.height

    def get_perimeter(self):
        # Perimeter = 2 × (width + height)
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Diagonal via Pythagorean theorem: √(width² + height²)
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        # Reject shapes too large to draw
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Build a grid of '*' characters: each row is width stars, repeated height times
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        # Integer-divide both axes to find how many times shape fits (no rotation)
        return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # A square is a rectangle where width == height
        super().__init__(side, side)

    def set_width(self, width):
        # Overrides Rectangle.set_width to keep both dimensions equal
        self.width = self.height = width

    def set_height(self, height):
        # Overrides Rectangle.set_height to keep both dimensions equal
        self.width = self.height = height

    def set_side(self, side):
        # Convenience method specific to Square
        self.width = self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"