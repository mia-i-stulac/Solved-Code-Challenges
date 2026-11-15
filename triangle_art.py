# So for this LinkedinLearning challenge, I was given a parent-child class of Shape and Square (the child class prints a square)
# I needed to add a triangle class that prints a triangle.
# I needed to modify it to create various triangle versions, the guidelines were very flexible.
# Basically, I could finish the challenge as soon as I felt like I made enough different triangles. 
# So I made the following: Equilateral (double size), right triangle, upside down right triangle. 
# This took me about an hour and I still feel like I will feel like I can learn more after watching her solution, but I am proud of what I accomplished!

# Note: The border shows what code I was given to work with initially

# _________________________________________________________________________________________________________________________________________________________
class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)
# _________________________________________________________________________________________________________________________________________________________
class Triangle(Shape):
# This prints an upside down right triangle
	def print(self):
		for i in range(self.height):
			self.printRow(i)
			self.width -= 1

	def printRow(self, i):
		print(self.printChar * self.width)
			
class RightTriangle(Triangle):
	# This prints an upside right triangle
	width = 0
	def print(self):
		for i in range(self.height):
			self.width += 1
			self.printRow(i)

class EquilateralTriangle(Shape):
  #This prints a double sized equilateral right triangle (upside down)
  # I couldn't quite figure out how to do the normal right triangle...
	space = ' '
	counter = 0
	def print(self):
		for i in range(self.height):
			if self.width < self.height:
				print((self.space * self.counter) + (self.printChar * (self.width* 2)) + (self.space * self.counter))
				self.counter += 1
			self.width -= 1
