#OOPSFact.py
class Fact:
	def factnum(self):
		self.n = int(input("Enter a number :"))
		fact = 1
		for i in range(1,self.n+1):
			fact = fact*i
		#return fact
		print(fact)
			

#Main program
f=Fact()
f.factnum()