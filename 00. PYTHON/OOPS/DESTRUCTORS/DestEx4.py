#Program for Demonstrating the NEED of Destructor
#DestEx4.py
import time
class Employee:
	def __init__(self,eno,name):  # Constructor Definition
		print("I am from Parameterized  Constructor")
		self.eno=eno
		self.name=name
		print("\t{}\t{}".format(self.eno,self.name))
	def __del__(self): # Destructor Definition
		print("\tGC calls __del__() for De-allocating the memory space:")

#Main Program
print("Program Execution Started")
eo1=Employee(10,"RS") # Object Creation--Makes the PVM to call Parameterized Constructor
print("No Longer interested to maintain eo1 object memory space")
time.sleep(5)
del eo1 #GC calls Destructor Forcefully 
time.sleep(5)
eo2=Employee(20,"TR") # Object Creation--Makes the PVM to call Parameterized Constructor
print("No Longer interested to maintain eo2 object memory space")
time.sleep(5)
del eo2 #GC calls Destructor Forcefully 
time.sleep(5)
eo3=Employee(30,"MC") # Object Creation--Makes the PVM to call Parameterized Constructor
print("No Longer interested to maintain eo3 object memory space")
time.sleep(5)
del eo3 #GC calls Destructor Forcefully 
time.sleep(5)
print("Program Execution Ended")
