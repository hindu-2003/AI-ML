#Program for Demonstrating Decorator
#Non-DecEx1.py
def  getval():  # Normal Function Defined by KVR
	return 5

def square():					#Apurva asked ,sir give  5**2 as ANS to me
	n=getval()
	print("square({})={}".format(n,n**2))

def squareroot():					#Anitha Teacher asked me sir give  5**0.5 as ANS to me
	n=getval()
	print("squareroot({})={}".format(n,n**0.5))

def cube():				# Sudha asked me sir 5**3 as ANS to me
	n=getval()
	print("cuberoot({})={}".format(n,n**3))

#Main Program
square()
squareroot()
cube()