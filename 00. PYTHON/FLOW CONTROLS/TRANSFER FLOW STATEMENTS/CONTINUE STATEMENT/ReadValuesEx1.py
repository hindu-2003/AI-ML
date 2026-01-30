#program for Reading Values from Key Board and display
#ReadValuesEx1.py
nov=int(input("How Many Values u want to Enter:"))
if(nov<=0):
    print("{} is Invalid Input".format(nov))
else:
    lst=[] # Create an empty list Or lst=list()
    for i in range(1,nov+1):
        value=input("Enter {} Value:".format(i))
        lst.append(value)
    else:
        print("Given List of Values=",lst)