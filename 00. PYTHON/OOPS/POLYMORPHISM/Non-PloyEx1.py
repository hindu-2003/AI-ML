#Non-PloyEx1.py ( Inheritance Program)
class Circle:
	def draw1(self):
		print("Drawing Circle:")

class Rect(Circle):
	def draw2(self):
		print("Drawing Rect:")

#main program
r=Rect()
r.draw1()
r.draw2()