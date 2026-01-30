#Program for Demonstrating Need of Static Method
#StaticMethodEx6.py
class Employee:
    def readempdata(self):
        print('-'*50)
        self.eno=int(input("\tEnter Employee Number:"))
        self.ename=input("\tEnter Employee Name:")
        self.sal=float(input("\tEnter Employee Salary:"))
        Hyd.dispobjinfo(self,"Employee")

class Student:
    def readstudata(self):
        print('-'*50)
        self.sno = int(input("\tEnter Student Number:"))
        self.sname = input("\tEnter Student Name:")
        Hyd.dispobjinfo(self, "Student")
class Teacher:
    def readteacherdata(self):
        print('-'*50)
        self.tno = int(input("\tEnter Teacher Number:"))
        self.tname = input("\tEnter Teacher Name:")
        self.subject = input("\tEnter Teacher Subject:")
        self.exp=float(input("\tEnter Teacher Experience:"))
        Hyd.dispobjinfo(self, "Teacher")
class Hyd:
    @staticmethod
    def dispobjinfo(obj,objinfo):
        print("*"*50)
        print("{} Information".format(objinfo))
        print("*"*50)
        for k,v in obj.__dict__.items():
            print("\t{}--->{}".format(k,v))
        print("*" * 50)
#Main Program
eo=Employee()
so=Student()
to=Teacher()
#read the data for Different Objects
eo.readempdata()
so.readstudata()
to.readteacherdata()
