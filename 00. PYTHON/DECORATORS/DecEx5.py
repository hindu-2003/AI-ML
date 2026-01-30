#Program for Demonstrating Decorator
#DecEx5.py
def reversewords(clow):
	def reverseword():
		line,UL,LL=clow()
		rlst=[]
		for word in line.split():
			rlst.append(word[::-1])
		return line,UL,LL," ".join(rlst)
	return reverseword

def convertlower(cup):
	def converlow():
		line,UL=cup()
		return line,UL,line.lower()
	return converlow

def convertupper(gl):
	def converup():
		line=gl()
		return line,line.upper()
	return converup

@reversewords
@convertlower
@convertupper
def getLine():
	return input("Enter a line of Text:")

#Main Program
NL,UL,LL,rwd=getLine()
print("\tGiven Line of Text:{}".format(NL))
print("\tUpper Case Text:{}".format(UL))
print("\tLower Case Text:{}".format(LL))
print("\tReversed Text:{}".format(rwd.upper()))
print("\tReversed Text:{}".format(rwd.lower()))
