#Program for Demonstrating the NEED of Destructor
#DestEx1.py
import time
class Employee:
	def __init__(self,eno,name):  # Constructor Definition
		print("\tI am from Parameterized  Constructor")
		self.eno=eno
		self.name=name
		print("\t{}\t{}".format(self.eno,self.name))
	def __del__(self): # Destructor Definition
		print("\tGC calls __del__() for De-allocating the memory space:")

#Main Program
print("Program Execution Started")
eo1=Employee(10,"RS") # Object Creation--Makes the PVM to call Parameterized Constructor
eo2=Employee(20,"TR") # Object Creation--Makes the PVM to call Parameterized Constructor
eo3=Employee(30,"MC") # Object Creation--Makes the PVM to call Parameterized Constructor
print("Program Execution Ended")
time.sleep(5)