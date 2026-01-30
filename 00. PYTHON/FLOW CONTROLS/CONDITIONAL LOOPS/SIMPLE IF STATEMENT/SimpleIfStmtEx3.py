#progrm for finding biggest of Three Numbers and check for equality
#SimpleIfStmtEx3.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
#logic a big
if (b<=a>c):
    print("Big({},{},{})={}".format(a,b,c,a))
#logic b big
if(a<b>=c):
    print("big({},{},{})={}".format(a,b,c,b))
#logic c big
if(a<=c>b):
    print("big({},{},{})={}".format(a,b,c,c))
#equality
if(a==b==c):
    print("All Values are equal")
