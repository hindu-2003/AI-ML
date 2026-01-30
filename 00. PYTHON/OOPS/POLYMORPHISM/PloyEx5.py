#PloyEx5.py 
class Circle:
	def draw(self): # Original Method
		print("Drawing Circle:")
	
class Rect:
	def draw(self):# Original Method
		print("Drawing Rect")
		
class Square(Circle,Rect):
	def draw(self): # Overridden Method
		print("Drawing Square")
		super().draw()
		#super().draw() Not Possible to call draw() of Rect Class
		Rect.draw(self)
	
#main Program
s=Square()
s.draw()