#Program for Demonstrating Generator
#GenEx4.py
def  getcourses():
	yield "PYTHON"
	yield "HTML"
	yield "C"
	yield "C++"


#Main Program
nitcrs=getcourses()
print("Type of nitcrs=",type(nitcrs))
print(next(nitcrs))
print(next(nitcrs))
print(next(nitcrs))
print(next(nitcrs))
#print(next(nitcrs))----Gives StopIteration .
