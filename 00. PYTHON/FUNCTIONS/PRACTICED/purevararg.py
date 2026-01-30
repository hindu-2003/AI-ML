#Program for finding sum of Variable length Numerical values
def findtotal(sno, sname, *m, city="hyd", crs="Python"):
    print("---------------------------------")
    print("Student number :{}".format(sno))
    print("Student Name :{}".format(sname))
    print("city Name :{}".format(city))
    print("course Name :{}".format(crs))
    print("="*50)
    s = 0
    for val in m:
        print(val, end=" ")
        s = s+val
    print()
    print("Sum=", s)
    print("="*50)
#Main program
findtotal(100, "MB", 10, 20, 30, 40, 50)
findtotal(100, "RS", 12, 25, 0, 25, 6)
findtotal(100, "SR", 10, 20, 40, 50)
findtotal(100, "PR", 10, 20)
findtotal(100, "VD", 10, 20, 30, 23.5)
findtotal(100, "AR")
findtotal(100, "ST", 10, 100, 50)
findtotal(100, "JI", 10, 20, 30, 50)


