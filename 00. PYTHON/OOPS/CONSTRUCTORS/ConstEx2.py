#Program for Demonstrating Creating an Object and Placing the Data
#ConstEx2.py
class Student:
	def __init__(self,sno,sname,marks): # Parametrized Constructor Definition
		print("I am from Parametrized Constructor")
		self.sno=sno
		self.name=sname
		self.marks=marks
		print(self.sno,self.name,self.marks)

#Main Program
s1=Student(100,"RS",45.67) # Object Creation--Makes the PVM to Call Parametrized Constructor Automatically
s2=Student(200,"TR",66.67) # Object Creation--Makes the PVM to Call Parametrized Constructor Automatically
s3=Student(300,"MC",76.67) # Object Creation--Makes the PVM to Call Parametrized Constructor Automatically

