from raiseDiv1 import divop
from rclass import DivsionByZeroError
while(True):
    try:
        a = int(input("Enter First Value:"))
        b = int(input("Enter Second Value:"))
        try:
            res=divop(a,b) # Function call---gives Exception or Result
        except DivsionByZeroError:
            print("\tDon't Enter Zero for Den...")
        else:
            print("Div({},{})={}".format(a,b,res))
            break
    except ValueError:
        print("\tDon't enter alnums,strs and symbols")