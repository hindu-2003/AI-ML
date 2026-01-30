#Program for Demonstrating Decorator
#DecEx1.py
def getval():
	return float(input("Enter Any Numerical value:"))

def square(gv): # Decorator
	print("Decorator Called")
	def calculate(): # Inner Function
		print("Inner Function calling")
		n=gv()
		res=n**2
		return res
	return calculate
	
#Main Program
kvr=square(getval) # Decorator  Call
print("type of kvr=",type(kvr))
res=kvr()
print("Square=",res)