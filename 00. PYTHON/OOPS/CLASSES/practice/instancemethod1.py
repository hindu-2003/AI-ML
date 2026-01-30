class Student:
    def stddet(self,a):
        self.sno = 10
        self.name = "Mounika"
        self.marks = 26
        print("{} Student number {} :".format(a,self.sno))
        print("{} Student number {} : ".format(a,self.name))
        print("{} Student number {} :".format(a,self.marks))
        print("{} Student number {} :".format(a,self.cnt))

Student.cnt = "India"
s1 = Student()
s1.stddet("First")
