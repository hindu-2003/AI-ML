# Write a python program which will find max of 3 numbers by using anonymous functions
# AnonymousEx7.py
findmax=lambda a, b, c:  b if a < b > c else a if b < a > c else c if b < c > a else "All are equal"
#Main program
a,b,c=float(input("Enter first value:")),float(input("Enter second value:")),float(input("Enter third value:"))
res=findmax(a,b,c)
print("Max value in {} ,{} and {} is : {} ".format(a,b,c, res))





