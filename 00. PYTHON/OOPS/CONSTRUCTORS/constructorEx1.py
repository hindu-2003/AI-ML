#constructorEx1.py
# Program for demonstrating Constructor ?
class Test:
	def __init__(self):
		print("constructor Execution")
	def m1(self):
		print("Instance Excution")
t = Test()   # constructor Execution with out creating object intialize the object
t.m1()        # Instance Excution with calling instance method to class