class emp:
    @classmethod
    def emp(cls,a):
        cls.eno = 100
        cls.name = "mahesh"
        print("\t {} Employee details ".format(a))
        print("{} Employee number :{}".format(a,cls.eno))
        print("{} Employee name :{}".format(a,cls.name))
e = emp()

e.emp("First")
#e1.dis("Second")

