#Program for Finding  max and minfrom List of  Numbers by using Anonymous Functions
#Don't use Pre-Defined max() and min()
#AnonymousFunEx4.py
def kvrmax(lst):   # lst=[10,20,4,5,25,3]
    if(len(lst)==0):
        return "Can't file Max bcoz list is empty"
    elif(len(set(lst))==1):
        return "All Values are equal"
    elif(len(lst)>1):
        maxv=lst[0]
        for val in lst:
            if(val>maxv):
                maxv=val
        return maxv
def kvrmin(lst):   # lst=[10,20,4,5,25,3]
    if(len(lst)==0):
        return "Can't file Min bcoz list is empty"
    elif(len(set(lst))==1):
        return "All Values are equal"
    elif(len(lst)>1):
        minv=lst[0]
        for val in lst:
            if(val<minv):
                minv=val
        return minv

findmax=lambda lst:kvrmax(lst) # Anonymous Function calling Normal Function
findmin=lambda lst:kvrmin(lst) # Anonymous Function calling Normal Function
#Main Program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split()]
maxv=findmax(lst) # Anonymous Function Call
minv=findmin(lst) # Anonymous Function Call
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))