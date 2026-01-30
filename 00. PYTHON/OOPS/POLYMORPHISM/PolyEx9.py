#Program for Cal Area of different figures such as Circle,Square,Rect by using OOPS--Polymorphism
#PolyEx9.py
class Circle:
	def  area(self): # Original Method
		self.r=float(input("Enter Radius:"))
		self.ac=3.14*self.r**2
		print("Area of Circle=",self.ac)
class Square(Circle):
	def area(self): # Overridden Method
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square=",self.sa)
		print("--------------------------------------------")
		super().area()
class Rect(Square):
	def area(self): # Overridden Method
		self.L,self.B=float(input("Enter Legth:")),float(input("Enter Breadth:"))
		self.ra=self.L*self.B
		print("Area of Rect=",self.ra)
		print("------------------------------------------")
		super().area()

#Main Program
r=Rect()
r.area()

		