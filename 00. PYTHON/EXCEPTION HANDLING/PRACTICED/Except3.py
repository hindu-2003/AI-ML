import os
try:
    s1=int(input("enter 1st  number"))
    s2= int(input("enter 2nd  number"))
    c = s1/s2
    print(c)
except Exception:
    print("Exception hit")
try:
    s1 = int(input("enter 1st number"))
    s2 = int(input("enter 2nd number"))
    c = s1 + s2
    print(c)
    os._exit()
except Exception:
    print("Exc2")
else:
    print("Else is working")
finally:
    print("finally output")
