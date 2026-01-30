#Program for Demonstrating Instance Methods
#InstanceMethodEx1.py
class Student:
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
        print("-------------------------------------------")
    def dispstuddata(self,objinfo):
        print("{} Object Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-------------------------------------------")

#main Program
#create an object of student
s1=Student()
s2=Student()
print("content of s1=",s1.__dict__)
print("content of s2=",s2.__dict__)
#Read Instance Data for s1
s1.readstuddata("First")
#Read Instance Data for s2
s2.readstuddata("Second")
#Display First Student Data
s1.dispstuddata("First")
#Display Second Student Data
s2.dispstuddata("Second")

