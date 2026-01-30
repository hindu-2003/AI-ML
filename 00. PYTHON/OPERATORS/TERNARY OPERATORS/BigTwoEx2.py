#Program for finding biggest of two numbers and check for equality by using Ternary Operator
#BigTwoEx2.py
a=float(input("Enter First Value:")) # 20
b=float(input("Enter Second Value:")) # 20
#logic for big and equality
res=a if a>b else b  if b>a else "Both Values are equal"
print("big({},{})={}".format(a,b,res))
