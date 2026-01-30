#Program for Cal Area of different figures such as Circle,Square,Rect by using OOPS--Polymorphism
#PolyEx12.py
class Circle:
	def  area(self,r): # Original Method
		self.ac=3.14*r**2
		print("Area of Circle=",self.ac)
class Square:
	def area(self,s): # Original Method
		self.sa=s**2
		print("Area of Square=",self.sa)
		
class Rect(Circle,Square):
	def area(self,L,B): # Overridden Method
		self.ra=L*B
		print("Area of Rect=",self.ra)
		print("------------------------------------------")
		super().area(float(input("Enter Radius:")))
		print("--------------------------------------------")
		Square.area(self,float(input("Enter Side:")))
		
#Main Program
r=Rect()
L,B=float(input("Enter Legth:")),float(input("Enter Breadth:"))
r.area(L,B)

		