#PloyEx1.py 
class Circle:
	def draw(self): # Original Method
		print("Drawing Circle:")
	
class Rect(Circle):
	def draw(self): # Overridden Method
		print("Drawing Rect")
		super().draw()


#main Program
r=Rect()
r.draw()