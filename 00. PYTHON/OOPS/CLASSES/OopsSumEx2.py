#Program for Adding of Two Numbers by using Classes and Objects
#OopsSumEx2.py
class Sum:
	def getvals(self):
		self.a=float(input("Enter First value:"))
		self.b=float(input("Enter Second value:"))
	def addvals(self):
			self.c=self.a+self.b
	def dispvals(self):
		print("sum({},{})={}".format(self.a,self.b,self.c))
	
#Main Program
s=Sum()
s.getvals()
s.addvals()
s.dispvals()
