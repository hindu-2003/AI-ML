#program for Swapping any Two Integer Values
#AssignmentOpEx3.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("Original value of a:{}".format(a))
print("Original value of b:{}".format(b))
print("-"*50)
#Swapping Logic
a=a*b
b=a//b
a=a//b
print("Swapped value of a:{}".format(a))
print("Swapped value of b:{}".format(b))
print("-"*50)
