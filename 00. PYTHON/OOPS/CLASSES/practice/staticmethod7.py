#staticmethod5.py
class Student:
    def readstudent(self):
        print(" STUDENT DETAILS ")
        print("=" * 50)
        self.sno = int(input("\tEnter Student Number :"))
        self.name =input("\tEnter Student name :")
        self.marks = float(input("\tEnter Student marks :"))
        nit.display(self,"Student")
class Employee:
    def reademp(self):
        print("*" * 50)
        print(" EMPLOYEE DETAILS ")
        print("=" * 50)
        self.eno = int(input("\tEnter Employee Number :"))
        self.name = input("\tEnter Employee Name :")
        self.sal = float(input("\tEnter Employee salary :"))
        nit.display(self,"Employee")
class Teacher:
    def readteach(self):
        print("*" * 50)
        print(" TEACHER DETAILS ")
        print("=" * 50)
        self.name = (input("\tEnter Teacher Name :"))
        self.sub = input("\tEnter Teacher Subject :")
        self.sal = float(input("\tEnter Teacher salary :"))
        nit.display(self,"Teacher")
while(1):
    try:
        class nit:
            def recieve(self,obj,objinfo):
                self.display(obj,objinfo)   # calling Static Method from Instance Method w.r.t cls
            @staticmethod
            def display(obj,objinfo):
                print("_"*50)
                print("\t {} Information".format(objinfo))
                print("=" * 50)
                for k,v in obj.__dict__.items():
                    print("\t\t{} --------> {}".format(k,v))
                print("=" * 50)

        # object creation for class
        s = Student()
        e = Employee()
        t = Teacher()
        # call to instance method w.r.t object name
        print("=" * 50)
        s.readstudent()
        e.reademp()
        t.readteach()
        break
    except ValueError:
        print("Don't enter useless things while enter keyboard you must read")



