#PloyEx4.py 
class Circle:
	def draw(self): # Original Method
		print("Drawing Circle:")
	
class Rect(Circle):
	def draw(self): # Overridden Method
		print("Drawing Rect")
		
class Square(Rect):
	def draw(self): # Overridden Method
		print("Drawing Square")
		Circle.draw(self) # Class Name approach

	
#main Program
s=Square()
s.draw()