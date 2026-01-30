#Write a Python program to get the smallest number from a list.
#LIST_Q4.py
def list_sum():
    nov = int(input("Enter how many values u r want:"))
    if nov<=0:
        print("PLease enter least one value for list creation")
    else:
        slst = []
        lst = []
        for i in range(1,nov+1):
            val=(input("Enter {} the values:".format(i)))
            lst.append(val)
        print("\tList is created {}".format(lst))
        lst.sort()
        print("\tList is sorted {}".format(lst))
        print("*"*50)

        s = []
        for j in lst:
            if j.isdigit():
                print("\t{}".format(j))
                s.append(int(j))
                s.sort()
            # elif len(lst) == 0:
            #     print("No integer data found --try again")
            elif type(j) == str:
                slst.append(j)
            elif type(j) == float:
                lst.append(float(j))
            elif type(j) == complex:
                slst.append(j)
            elif type(j) == bool:
                slst.append(j)
                slst.sort()
            else:pass
        print("-" * 50)

    print("\t\t list Numbers {} and smallest number is :{}".format(s,s[0]))
    print("=" * 50)
    print("""In this list out of integer values i gotted . 
So, I can also give  multiple type of values in small (string, bool, complex, float)Data Types:{}""".format(slst))
    print("=" * 50)
print(list_sum())


