#Program for Finding Sum and Average of List of Values by using Function
#SumAvgInnerFunEx
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

def findsumavg():
    lstobj=readvalues() # One function calling another function--called Function Chaining
    if(len(lstobj)==0):
        print("No Values Present-can't find Sum and Average")
    else:
        s=0
        for val in lstobj:
            s=s+val
        else:
            print("------------------------------------------")
            print("Given List of Elements={}".format(lstobj))
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lstobj)))
            print("------------------------------------------")
#Main Program
findsumavg() # function call
