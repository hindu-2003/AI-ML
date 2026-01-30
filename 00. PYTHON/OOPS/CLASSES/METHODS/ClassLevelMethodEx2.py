#Program for Demonstrating Class Level method
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrses(cls):
        cls.crs="Python"  # here crs  is called Class Level Data Members
        cls.getuname() # calling Class Level method w.r.t cls
        #OR Student.getuname() # calling Class Level method w.r.t Student
    @classmethod
    def getuname(cls):
        cls.uname="JNTU-HYD" # here uname  is called Class Level Data Members

#main Program
Student.getcrses() # calling Class Level Method By using Class name  ===========>Method calling
print("Course=",Student.crs)
print("Student University=",Student.uname)
print("----------------OR--------------------")
s1=Student()
s1.getcrses() # calling Class Level Method By using Object name
print("Course=",s1.crs)
print("Student University=",s1.uname)
