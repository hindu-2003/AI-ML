#program for Reading Values from Key Board  and find sum and average
#ReadValuesEx4.py
lst=[] # create an empty list
while(True):
    value=input("Enter Value(Press @ to stop):")
    if(value=="@"):
        break
    else:
        lst.append(float(value))
print("--------------------------------")
print("Content of List=",lst) # [12.0, 2.3, 4.5, 34.56, 34.0, 56.0]
print("--------------------------------")
#Code for Finding Sum  and Avg of Elements of List
s=0
for val in lst:
    s=s+val
else:
    print("Sum={}".format(s))
    print("Avg={}".format(s/len(lst)))
    print("--------------------------------")


