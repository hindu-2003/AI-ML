#staticmethod1.py
class Student:
    def readstudent(self):
        print(" STUDENT DETAILS ")
        print("=" * 50)
        self.sno = int(input("\tEnter Student Number :"))
        self.name =input("\tEnter Student name :")
        self.marks = float(input("\tEnter Student marks :"))
class Employee:
    def reademp(self):
        print("*" * 50)
        print(" EMPLOYEE DETAILS ")
        print("=" * 50)
        self.eno = int(input("\tEnter Employee Number :"))
        self.name = input("\tEnter Employee Name :")
        self.sal = float(input("\tEnter Employee salary :"))
class Teacher:
    def readteach(self):
        print("*" * 50)
        print(" TEACHER DETAILS ")
        print("=" * 50)
        self.name = (input("\tEnter Teacher Name :"))
        self.sub = input("\tEnter Teacher Subject :")
        self.sal = float(input("\tEnter Teacher salary :"))
while(1):
    try:
        class nit:
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
        # Display the Data of Different Objects of Different Classes
        # By using Single Method called Static Method
        # display the above data with static method
        nit().display(s,"Student")  # calling static method by using Class Name
        nit().display(e,"Employee")  # calling static method by using Class Name
        nit().display(t,"Teacher")  # calling static method by using Class Name
        break
    except ValueError:
        print("Don't enter useless things while enter keyboard you must read")



