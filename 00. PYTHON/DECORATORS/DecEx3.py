#Program for Demonstrating Decorator
#DecEx3.py
def square(gv):
	def calculate():
		n=gv()
		res=n**2
		return n,res
	return calculate

@square
def getval():
	return float(input("Enter Any Numerical value:"))

#Main Program
num,result=getval() # Normal Function call
print("Square({})={}".format(num,result))