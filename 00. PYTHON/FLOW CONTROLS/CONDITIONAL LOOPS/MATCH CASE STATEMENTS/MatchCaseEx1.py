#MatchCaseEx1.py
import sys
print("="*50)
print("\tARITHMETIC OPERATIONS")
print("="*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Div")
print("\t6.Exponentiation")
print("\t7.Exit")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter two Values for Addition")
        a,b=float(input()),float(input())
        print("Sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter two Values for Substraction")
        a, b = float(input()), float(input())
        print("Sub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter two Values for Multiplication")
        a, b = float(input()), float(input())
        print("Mul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter two Values for Division")
        a, b = float(input()), float(input())
        print("Div({},{})={}".format(a, b, a / b))
        print("FloorDiv({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter two Values for Modulo Div")
        a, b = float(input()), float(input())
        print("Mod({},{})={}".format(a, b, a % b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("pow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for using program")
    case _:
        print("Ur selection of Operation is wrong--try again")
print("Program execution completed")

