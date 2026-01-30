#Program for Demonstrating the NEED of Destructor
#DestEx5.py
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
eo2=eo1 # Deep Copy
eo3=eo1 # Deep Copy
print("No Longer interested to maintain eo1 object memory space")
time.sleep(5)
del eo1 #GC will not call Destructor Forcefully  bcoz still eo2 and eo3 Pointing to Object
time.sleep(5)
print("No Longer interested to maintain eo2 object memory space")
time.sleep(5)
del eo2 #GC will not call Destructor Forcefully  bcoz still  eo3 Pointing to Object
time.sleep(5)
print("No Longer interested to maintain eo3 object memory space")
time.sleep(5)
del eo3 #GC calls Destructor Forcefully bcoz still   objects are not  Pointing to Object memory space
time.sleep(5)
print("Program Execution Ended")
