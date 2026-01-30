#Program for Calculating Factorial of a Given Number by using Classes and Objects
#OopsFactEx1.py
class Fact:
	def getval(self):
		self.n=int(input("Enter a Number for cal Factorial:"))
	def calFact(self):
		if(self.n<0):
			return("For -VE Number, There is No factorial")
		else:
			fact=1
			for i in range(1,self.n+1):
				fact=fact*i
			return fact
	
	def dispresult(self):
		print("Factorial({})={}".format(self.n,self.calFact()))

#Main Program
fo=Fact()
fo.getval()
fo.calFact()
fo.dispresult()


