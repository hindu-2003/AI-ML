#program for Reading Values from Key Board and display
#ReadValuesEx2.py
nov=int(input("How Many Values u want to Enter:")) # 5
if(nov<=0):
    print("{} is Invalid Input".format(nov))
else:
    lst=list() # Creating an empty List for storing Dynamic values
    i=1
    while(i<=nov):
        val=input("Enter {} Value:".format(i))
        lst.append(val)
        i+=1
    else:
        print("Content of List=",lst)