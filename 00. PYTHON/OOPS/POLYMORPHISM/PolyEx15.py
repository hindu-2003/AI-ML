#Program for Cal Area of different figures such as Circle,Square,Rect by using OOPS--Polymorphism
#PolyEx15.py
class Circle:
	def  __init__(self,r): # Original Constructor
		self.ac=3.14*r**2
		print("Area of Circle=",self.ac)
class Square:
	def __init__(self,s): # Original Constructor
		self.sa=s**2
		print("Area of Square=",self.sa)
		
class Rect(Circle,Square):
	def __init__(self,L,B): # Overridden Constructor
		self.ra=L*B
		print("Area of Rect=",self.ra)
		print("------------------------------------------")
		super().__init__(float(input("Enter Radius:")))
		print("--------------------------------------------")
		Square.__init__(self,float(input("Enter Side:")))
		
#Main Program
r=Rect(float(input("Enter Legth:")),float(input("Enter Breadth:")) )



		