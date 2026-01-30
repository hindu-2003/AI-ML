#Program for Cal Area of different figures such as Circle,Square,Rect by using OOPS--Polymorphism
#PolyEx13.py
class Circle:
	def  __init__(self): # Original Constructor
		self.r=float(input("Enter Radius:"))
		self.ac=3.14*self.r**2
		print("Area of Circle=",self.ac)
class Square(Circle):
	def __init__(self): # Overridden Constructor
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square=",self.sa)
		print("--------------------------------------------")
		super().__init__()
		
class Rect(Square):
	def __init__(self): # Overridden Constructor
		self.L,self.B=float(input("Enter Legth:")),float(input("Enter Breadth:"))
		self.ra=self.L*self.B
		print("Area of Rect=",self.ra)
		print("------------------------------------------")
		super().__init__()
		

#Main Program
r=Rect()


		