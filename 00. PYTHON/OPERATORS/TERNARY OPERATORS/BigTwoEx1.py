#Program for finding biggest of two numbers by using Ternary Operator
#BigTwoEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
#logic for big
bigv=a if a>b else b
print("Big({},{})={}".format(a,b,bigv))