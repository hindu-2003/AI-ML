#Program for Calculating Factorial of a Given Number by using Classes and Objects
#OopsFactEx2.py
class Fact:
	def getval(self):
		while(True):
			try:
				self.n=int(input("Enter a Number for cal Factorial:"))
			except ValueError:
				print("\tInvalid Input--try again")
			else:
				break
	def calFact(self):
		if(self.n<0):
			return("For -VE Number, There is No factorial")
		else:
			fact=1
			for i in range(1,self.n+1):
				fact=fact*i
			return fact
	
	def dispresult(self):
		self.getval()
		print("Factorial({})={}".format(self.n,self.calFact()))

#Main Program
Fact().dispresult()


