#Program for Demonstrating the NEED of Inheritance
#InhProgEx3.py
class C1:
	def getA(self):
		self.a=10

class C2:
	def getB(self):
		self.b=20

class C3(C1,C2):
	def operation(self):
		self.c=self.a+self.b
		print("sum({},{})={}".format(self.a,self.b,self.c))
		

#Main Program
o3=C3()
o3.getA()
o3.getB()
o3.operation()
