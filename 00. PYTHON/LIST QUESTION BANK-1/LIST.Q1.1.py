#Write a Python program to multiplication all the items in a list.
#L1_Q2.py

nov = int(input("Enter how many values u r U want:"))
if nov<=0:
    print("PLease enter least one value for list creation")
else:
    lst = []
    s = 0
    for i in range(1,nov+1):
        val=(input("enter {} the values:".format(i)))
        k = int(val)
        if type(k)==int:
            lst.append(k)
    s = s + k
print("\t\tsum of list items {}".format(s))
print("=" * 50)




