#PloyEx3.py 
class Circle:
	def draw(self): # Original Method
		print("Drawing Circle:")
	
class Rect(Circle):
	def draw(self): # Overridden Method
		print("Drawing Rect")
		
class Square(Rect):
	def draw(self): # Overridden Method
		print("Drawing Square")
		Rect.draw(self) # Class Name approach
		Circle.draw(self) # Class Name approach

	
#main Program
s=Square()
s.draw()