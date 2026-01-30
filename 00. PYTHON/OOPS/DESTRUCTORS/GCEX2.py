#Program for Demonstrating the NEED of Destructor
#GCEX2.py
import time,sys,gc
class Employee:
	def __init__(self,eno,name):
		print("\tI am from Parameterized  Constructor whose id={}".format(id(self)))
		self.eno=eno
		self.name=name
		print("\t{}\t{}".format(self.eno,self.name))
	
	def __del__(self):
		global totmemspace
		print("\tGC calls __del__() for De-allocating the memory space of :{}".format(id(self)))
		totmemspace=totmemspace-sys.getsizeof(self)
		print("\tNow Available Memory Space={}".format(totmemspace))

#Main Program
print("----------------------------------------------------")
print("\tIs GC Running=",gc.isenabled())
print("----------------------------------------------------")
print("Program Execution Started")
eo1=Employee(10,"RS") # Object Creation--Makes the PVM to call Parameterized Constructor
eo2=Employee(20,"TR") # Object Creation--Makes the PVM to call Parameterized Constructor
gc.disable()
eo3=Employee(30,"MC") # Object Creation--Makes the PVM to call Parameterized Constructor
print("\tIs GC Running=",gc.isenabled())
totmemspace=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("Total Memory Space of all objects=",totmemspace)
print("Program Execution Ended")
time.sleep(10)
# Here all the objects memory space destroyed by Destructor by runnung Garbage Collector automatically at th end of Program execution. This kind of Garbage Collection is called Automatic garbage Collection.
