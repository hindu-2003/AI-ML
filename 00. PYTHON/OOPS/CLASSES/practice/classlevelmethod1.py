class student:
    @classmethod
    def std(cls):
        cls.sno = 10
        cls.name = "mahesh"

# main program
student.std()
print(student.sno)
print(cls.name)
