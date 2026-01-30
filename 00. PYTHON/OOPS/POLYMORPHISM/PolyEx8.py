#Program for Demonstrating Constructor Overriding
#PolyEx8.py
class Circle:
	def __init__(self): # Original Constructor
		print("Circle---Default Constructor")

class Rect:
	def __init__(self): # Original Constructor
		print("Rect---Default Constructor")
		
class Square(Rect,Circle): # Multiple Inheritance
	def __init__(self): # Overridden Constructor
		print("Square---Default Constructor")
		super().__init__() # OR    Rect.__init__(self)
		Circle.__init__(self)

#Main Program
s=Square() # Object Created