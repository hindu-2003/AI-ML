#Program for Demonstrating Default Constructor
#DefaultConstEx.py
class Test:
	def __init__(self): 
		print("I am from Default Constructor")
		self.a=1
		self.b=2
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))

#Main Program
t1=Test() # Object Creation--PVM Calls Default Constructor
t2=Test() # Object Creation--PVM Calls Default Constructor