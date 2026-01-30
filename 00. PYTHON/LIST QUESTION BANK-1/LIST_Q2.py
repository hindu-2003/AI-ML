#Write a Python program to multiplication all the items in a list.
#L1_Q2.py

nov = int(input("Enter how many values u r U want:"))
if nov<=0:
    print("PLease enter least one value for list creation")
else:
    lst = []
    for i in range(1,nov+1):
        val=(input("enter {} the values:".format(i)))
        lst.append(val)
    print("\t\tList is created {}".format(lst))
    slst = []
    s = []
    s = 1
    for j in lst:
        if j.isdigit():
            print("\t{}".format(j))
            s = s * int(j)
        # elif len(lst) == 0:
        #     print("No integer data found --try again")
        elif type(j) == str:
            slst.append(j)
        elif type(j) == float:
            slst.append(j)
        elif type(j) == complex:
            slst.append(j)
        elif type(j) == bool:
            slst.append(j)
        else:pass
    print("-" * 50)
print("\t\tmul of list items {}".format(s))
print("=" * 50)
print("""In this list out of integer values i gotted . 
So, I can't multiplication (string, bool, complex, float)Data Types:{}""".format(slst))
print("=" * 50)



