#ClassLevelDataMemberEx1.py
class Student:
    crs="PYTHON" # here crs is called Class level data members

#main Program
s1=Student()
print("Content of s1=",s1.__dict__)
print("Number of Values in s1=",len(s1.__dict__))
#Access the Class Level Member w.r.t Class Name
print("Course Name=",Student.crs)
#Access the Class Level Member w.r.t Object Name
print("Course Name=",s1.crs)
