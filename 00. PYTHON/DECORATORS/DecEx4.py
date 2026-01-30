#Program for Demonstrating Decorator
#DecEx4.py
def cube(opr):
	def cal():
		n,sqrv,sqrtval=opr()
		cb=n**3
		return n,sqrv,sqrtval,cb
	return cal

def squareroot(calc):
	def operation():
		n,sqrv=calc()
		sqrtval=n**0.5
		return n,sqrv,sqrtval
	return operation

def square(gv):
	def calculate():
		n=gv()
		res=n**2
		return n,res
	return calculate

@cube
@squareroot
@square
def getval():
	return float(input("Enter Any Numerical value:"))

#Main Program
n,sqv,sqrtv,cb=getval() # Normal Function call
print("Square({})={}".format(n,sqv))
print("SquareRoot({})={}".format(n,sqrtv))
print("Cube({})={}".format(n,cb))