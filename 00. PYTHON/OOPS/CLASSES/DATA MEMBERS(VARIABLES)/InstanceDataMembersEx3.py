#Program for Storing Student Deatils
#InstanceDataMembersEx3.py
class Student:pass

#main Program
s1=Student()
s2=Student()
print("-------------------------------")
print("Id of s1=",id(s1))
print("Content of s1=",s1.__dict__)
print("Number of Values in s1 object=",len(s1.__dict__))
print("Id of s2=",id(s2))
print("Content of s2=",s2.__dict__)
print("Number of Values in s2 object=",len(s2.__dict__))
print("-------------------------------")
#Place Instance Data members in S1 Object
s1.sno=10
s1.name="RS"
s1.marks=44.44
#Place Instance Data members in S2 Object
s2.stno=20
s2.name="TR"
s2.marks=66.66
s2.colname="NIT-Calicut"
#Display the Object s1 values
print("-------------------------------")
print("First Object s1 Values")
for idmn,idmv in s1.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("-------------------------------")
print("Second Object s2 Values")
for idmn,idmv in s2.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("-------------------------------")
print("--------------OR-----------------")
print("First Object s1 Values")
for idmn in s1.__dict__.keys():
    print("\t{}--->{}".format(idmn,s1.__dict__.get(idmn)))
print("-------------------------------")
print("Second Object s2 Values")
for idmn in s2.__dict__:
    print("\t{}--->{}".format(idmn,s2.__dict__[idmn]))
print("-------------------------------")

