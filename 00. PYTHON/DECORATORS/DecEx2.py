#Program for Demonstrating Decorator
#DecEx2.py
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
res=square(getval)() # Decorator Function call and It calls Its Inner Function
print("Square=",res)