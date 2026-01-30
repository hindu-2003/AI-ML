#MethodsNeed.py
class Student:
    crs="PYTHON" # here crs is called Class Level Data member

#Main Program
Student.cnt="INDIA"  # here cnt is called Class Level Data member of Student
s1=Student()
s2=Student()
#Place Instance Data members in S1 Object
s1.sno=int(input("Enter First Student Number:"))
s1.name=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
print("--------------------------------------------")
#Place Instance Data members in S2 Object
s2.stno=int(input("Enter Second Student Number:"))
s2.name=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
#Display S1 object Data (Instance Data members)
print("--------------------------------------------")
print("First Student Number=",s1.sno)
print("First Student Name=",s1.name)
print("First Student Marks=",s1.marks)
print("First Student Course=",s1.crs)
print("First Student Country=",s1.cnt)
print("--------------------------------------")
#Display S1 object Data (Instance Data members)
print("Second Student Number=",s2.stno)
print("Second Student Name=",s2.name)
print("Second Student Marks=",s2.marks)
print("Second Student Course=",s2.crs)
print("Second Student Country=",s2.cnt)
print("--------------------------------------")




