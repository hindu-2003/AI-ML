#Program for Adding of Two Numbers by using Classes and Objects
#OopsSumEx1.py
class Sum:pass


#main Program
s=Sum()
s.a=float(input("Enter First value:"))
s.b=float(input("Enter Second value:"))
s.c=s.a+s.b
print("Sum({},{})={}".format(s.a,s.b,s.c))
