#ClassLevelInstanceMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs = "Python"  # here crs  is called Class Level Data Members
        cls.getuname()
    @classmethod
    def getuname(cls):
        cls.uname = "JNTU-HYD" # here uname  is called Class Level Data Members
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
        print("-------------------------------------------")
    def dispstuddata(self,objinfo):
        self.getcrs() # calling Class Level Method w.r.t self from Instance Method
        print("{} Object Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("\tStudent Course:{}".format(Student.crs))
        print("\tStudent University:{}".format(Student.uname))
        print("-------------------------------------------")
#main Program
s1=Student()
s2=Student()
print(s1.__dict__)
print(s2.__dict__)
s1.readstuddata("First")
s2.readstuddata("Second")
s1.dispstuddata("First")
s2.dispstuddata("Second")