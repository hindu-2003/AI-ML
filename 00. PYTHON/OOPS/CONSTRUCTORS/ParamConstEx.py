#Program for Demonstrating Parameterized Constructor
#ParamConstEx.py
class Test:
	def __init__(self,a,b): 
		print("I am from Parameterized Constructor")
		self.a=a
		self.b=b
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))

#Main Program
t1=Test(10,20) # Object Creation--PVM Calls Parameterized Constructor
t2=Test(100,200) # Object Creation--PVM Calls Parameterized Constructor