#Program for Demonstrating Creating an Object and Placing the Data
#Non-ConstEx2.py
class Student:
	def readstuddata(self):
		self.sno=10
		self.name="RS"
		self.marks=44.44

#Main Program
s=Student()
print("content of s=",s.__dict__) # {}-----Step-1--Created Empty
# How can u place the data in object s
s.readstuddata() # We are calling the Method Explicitly--------Step-2-----placed Data
print("content of s=",s.__dict__) # {........}
