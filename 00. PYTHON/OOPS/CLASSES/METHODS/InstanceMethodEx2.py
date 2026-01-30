#Program for Demonstrating Instance Methods
#InstanceMethodEx1.py
class Student:
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
        print("-------------------------------------------")        
        self.dispstuddata(objinfo)          # calling Instance Method by using self.
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
#read s1 Data and Display
s1.readstuddata("First")
#read s2 Data and Display
s2.readstuddata("Second")