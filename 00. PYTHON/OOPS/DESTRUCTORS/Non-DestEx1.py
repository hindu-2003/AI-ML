#Program for Demonstrating the NEED of Destructor
#Non-DestEx1.py
class Employee:
	def __init__(self,eno,name):
		print("I am from Parameterized  Constructor")
		self.eno=eno
		self.name=name
		print(self.eno,self.name)

#Main Program
print("Program Execution Started")
eo1=Employee(10,"RS") # Object Creation--Makes the PVM to call Parameterized Constructor
eo2=Employee(20,"TR") # Object Creation--Makes the PVM to call Parameterized Constructor
eo3=Employee(30,"MC") # Object Creation--Makes the PVM to call Parameterized Constructor
print("Program Execution Ended")