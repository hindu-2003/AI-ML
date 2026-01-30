#Program for Demonstrating Constructor Overriding
#PolyEx7.py
class Circle:
	def __init__(self): # Original Constructor
		print("Circle---Default Constructor")

class Rect(Circle):
	def __init__(self): # Overridden Constructor
		print("Rect---Default Constructor")
		super().__init__()
		

class Square(Rect):
	def __init__(self): # Overridden Constructor
		print("Square---Default Constructor")
		super().__init__()
		

#Main Program
s=Square() # Object Created