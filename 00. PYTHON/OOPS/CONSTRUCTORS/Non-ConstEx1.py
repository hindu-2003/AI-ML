#Program for Demonstrating Creating an Object and Placing the Data
#Non-ConstEx1.py
class Student:pass

#Main Program
s=Student()
print("content of s=",s.__dict__) # {}-----Step-1--Created Empty
# How can u place the data in object s
s.sno=10
s.name="RS"
s.marks=45.67
print("content of s=",s.__dict__) # {........}-----Step-2-----placed Data
