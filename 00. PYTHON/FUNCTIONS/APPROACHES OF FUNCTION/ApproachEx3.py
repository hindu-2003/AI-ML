#Define a function for Adding of Two Numbers
#ApproachEx3.py
#Input:  Taken from Function Call
#Process:  Done in Function Body
#Output: Displayed in Function Body
def sumop(k,v):
    r=k+v
    print("Sum({},{})={}".format(k,v,r))

#Main Program
#Get Two values from KBD
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
sumop(k,v) # function call