#Program for Demonstrating Need of Static Method
#StaticMethodEx2.py
from Emp import Employee
from Student import Student
from Tea import Teacher
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
#Display the Data of Different Objects of Different Classes
#By using Single Method called Static Method
Hyd.dispobjinfo(eo,"Employee") # calling static method by using Class Name
Hyd.dispobjinfo(so,"Student") # calling static method by using Class Name
Hyd.dispobjinfo(to,"Teacher") # calling static method by using Class Name
