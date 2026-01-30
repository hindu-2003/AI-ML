#Program for Demonstrating writing Default and Parameterized Constructor
#DefaultParamConstEx.py
class Test:
	
	def __init__(self,a=1,b=2): 
		print("I am from Default / Parametrized Constructor")
		self.a=a
		self.b=b
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
	

#Main Program
# t1=Test() # Object Creation--PVM Calls Default Constructor
# t2=Test(10,20) # Object Creation--PVM Calls Parametrized Constructor
# t3=Test(100,200) # Object Creation--PVM Calls Parametrized Constructor
# t4=Test(300) # Object Creation--PVM Calls Parametrized Constructor
t5=Test(b=300) # Object Creation--PVM Calls Parametrized Constructor
t6=Test(b="Python",a="Django") # Object Creation--PVM Calls Parametrized Constructor