#Operations.py<---File Name and Module Name
def addop():
    print("Enter two values for addition:")
    a,b=float(input()),float(input())
    print("sum({},{})={}".format(a,b,a+b))
def subop():
    print("Enter two values for Substraction:")
    a, b = float(input()), float(input())
    print("sub({},{})={}".format(a, b, a - b))
def mulop():
    print("Enter two values for Multiplication:")
    a, b = float(input()), float(input())
    print("mul({},{})={}".format(a, b, a * b))
def divop():
    print("Enter two values for Division:")
    a, b = float(input()), float(input())
    print("Div({},{})={}".format(a, b, a / b))
    print("Floor Div({},{})={}".format(a, b, a // b))
def modop():
    print("Enter two values for Modulo Div:")
    a, b = float(input()), float(input())
    print("mod({},{})={}".format(a, b, a % b))
def expop():
    a, b = float(input("Enter Base:")), float(input("Enter Power:"))
    print("power({},{})={}".format(a, b, a ** b))