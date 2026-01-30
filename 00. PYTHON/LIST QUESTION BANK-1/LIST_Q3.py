#3. Write a Python program to get the largest number from a list.
#LIST_Q3.py
def list_sum():
    nov = int(input("Enter how many values are you want:"))
    if nov<=0:
        print("PLease enter least one value for list creation")
    else:
        slst = []
        lst = []
        for i in range(1,nov+1):
            val=(input("Enter {} the values:".format(i)))
            lst.append(val)
        print("\tList is created {}".format(lst))
        print("*"*50)

        s = []
        for j in lst:
            if j.isdigit():
                print("\t{}".format(j))
                s.append(int(j))
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
    print("\t\t list Numbers {} and largest number is :{}".format(s,max(s)))
    print("=" * 50)
    print("""In this list out of integer values i gotted . 
So, I can't multiplication (string, bool, complex, float)Data Types:{}""".format(slst))
    print("=" * 50)
print(list_sum())


