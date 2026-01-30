def stud(sno,name,marks,*x,city="HYD", crs="Python",**y): # crs and city are Default arguments
    print(x, type(x))
    print("S.No=",sno)
    print("Student name=",name)
    print('student marks=',marks)
    print(city)
    print(crs)
    print(y)

    print("_"*50)
# main program
stud(1,'Mahesh',50) # positional arguments
stud(marks=99,sno=10,name="Ab",city="chennai",crs="Java") # Key word arguments
stud(1,'Mahesh',50,10,20,30,city="Ban",state="Ts")  # variable length arguments
