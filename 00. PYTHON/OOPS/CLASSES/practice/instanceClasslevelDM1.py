class Student:
    crs = "python"
Student.cnt = "INDIA"
s1 = Student()
s2 = Student()
s1.sno = 10
s1.sname = "mahesh"
s1.marks = 99
s2.sno = 20
s2.sname = "Suresh"
s2.marks = 88
print("="*50)
print("Student number",s1.sname)
print("Student name:",s1.sname)
print("Student marks:",s1.marks)
print("Student courses:",s1.crs)
print("Student country:",s1.cnt)
print("="*50)
print("Student number",s2.sname)
print("Student name:",s2.sname)
print("Student marks:",s2.marks)
print("Student courses:",s2.crs)
print("Student country:",s2.cnt)
print("="*50)


