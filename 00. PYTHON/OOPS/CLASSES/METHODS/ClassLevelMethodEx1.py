#Program for Demonstrating Class Level method
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrses(cls):
        cls.crs="Python"
        Student.uname="JNTU" # here crs and uname are called Class Level Data Members

#main Program
Student.getcrses() # calling Class Level Method By using Class name
print("Course=",Student.crs)
print("Student University=",Student.uname)
print("----------------OR--------------------")
s1=Student()
s1.getcrses() # calling Class Level Method By using Object name
print("Course=",s1.crs)
print("Student University=",s1.uname)
