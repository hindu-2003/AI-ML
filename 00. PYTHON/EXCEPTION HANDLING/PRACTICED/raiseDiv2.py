from raiseDiv1 import divop
from rclass import DivsionByZeroError
try:
    a = int(input("Enter First Value:"))
    b = int(input("Enter Second Value:"))
    res=divop(a,b) # Function call---gives Exception or Result
except DivsionByZeroError:
    print("\tDon't Enter Zero for Den...")
except ValueError:
    print("\tDon't enter alnums,strs and symbols")
else:
    print("Div({},{})={}".format(a,b,res))
finally:
    print("I am from finally Block")
    print("Program Execution Completed")