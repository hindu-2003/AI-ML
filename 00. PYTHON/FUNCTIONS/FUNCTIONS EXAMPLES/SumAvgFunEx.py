#Program for Finding Sum and Average of List of Values by using Function
#SumAvgFunEx.py
def readvalues():
    nov=int(input("How Many Values sum and average u want find:"))
    if(nov<=0):
        return [] # Returning empty list OR return list()
    else:
        lst=[] # create an empty list for appending values
        for i in range(1,nov+1):
            val=float(input("Enter {} Value:".format(i)))
            lst.append(val)
        return lst

def findsumavg(lstobj): # lstobj=[10,20,30,40,50]
    if(len(lstobj)==0):
        print("No Values Present-can't find Sum and Average")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("------------------------------------------")
            print("Given List of Elements={}".format(lst))
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lstobj)))
            print("------------------------------------------")


#Main Program
lst=readvalues() # Function Call
findsumavg(lst) # function call
