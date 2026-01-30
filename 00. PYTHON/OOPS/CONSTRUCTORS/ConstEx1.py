#Program for Demonstrating Creating an Object and Placing the Data
#ConstEx1.py
class Student:
	def __init__(self): # Default OR Parameter Less  Constructor 
		print("I am from Default OR Parameter Less Constructor")
		self.sno=100
		self.name="RS"
		self.marks=45.67
		print(self.sno,self.name,self.marks)
		

#Main Program
s1=Student() # Object Creation--Makes the PVM to Call Default OR Parameter Less Constructor Automatically
s2=Student() # Object Creation--Makes the PVM to Call  Default OR Parameter Less Constructor Automatically
