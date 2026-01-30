#Program for Finding  Sum and Average by using Anonymous Functions
#AnonymousFunEx5.py
def sumavg(lst): # lst=[10,20,30,40]
        s=0
        for val in lst:
            s=s+val
        else:
            avg=s/len(lst)
            return s,avg

findsumavg=lambda lst: sumavg(lst)
#Main Program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
if(len(lst)==0):
        print("List is empty","Can't find sum and avg")
else:
    ss,av=findsumavg(lst)
    print("Sum({})={}\nAvg({})={}".format(lst,ss,lst,av))