#program for Reading Values from Key Board  until user press @ and display
#ReadValuesEx3.py
lst=[] # create an empty list
while(True):
    value=input("Enter Value(Press @ to Stop):")
    if(value=="@"):
        break
    else:
        lst.append(value)
print("Content of List=",lst)