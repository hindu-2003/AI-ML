#Program for Storing Student Deatils
#InstanceDataMembersEx1.py
class Student:pass

#Main Program
s1=Student()
s2=Student()
print("-------------------------------")
print("Id of s1=",id(s1))
print("Id of s2=",id(s2))
print("-------------------------------")
#Place Instance Data members in S1 Object
s1.sno=10
s1.name="RS"
s1.marks=44.44
#Place Instance Data members in S2 Object
s2.stno=20
s2.name="TR"
s2.marks=66.66
#Display S1 object Data (Instance Data members)
print("First Student Number=",s1.sno)
print("First Student Name=",s1.name)
print("First Student Marks=",s1.marks)
print("--------------------------------------")
#Display S1 object Data (Instance Data members)
print("Second Student Number=",s2.stno)
print("Second Student Name=",s2.name)
print("Second Student Marks=",s2.marks)
print("--------------------------------------")




