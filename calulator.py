# Shape Base Class
#You can analyze the common characteristics and find out that all of these are 2D shapes. Therefore, the best option is to create a class Shape with a method get_area() from which each shape will inherit.

# At the start of the file
from math import pi , sqrt
class Shape:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'

# Folded classes
class Shape: ...
class Rectangle(Shape): ...
    pass
 
class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)

# Folded classes
class Shape: ...
class Rectangle(Shape): ...
class Square(Rectangle): ...
 
class Triangle(Rectangle):
	def __init__(self, base, height):
		super().__init__(base, height)
 
	def get_area(self):
		area = super().get_area()
		return area / 2

# Folded classes
class Shape: ...
class Rectangle(Shape): ...
class Square(Rectangle): ...
class Triangle(Rectangle): ...

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
 
	def get_area(self):
		return pi * (self.radius ** 2)

# Folded classes
class Shape: ...
class Rectangle(Shape): ...
class Square(Rectangle): ...
class Triangle(Rectangle): …
class Circle(Shape): …
 
# Import square root
from math import sqrt
 
class Hexagon(Rectangle):
	
	def get_area(self):
		return (3 * sqrt(3) * self.side1 ** 2) / 2

breakpoint()