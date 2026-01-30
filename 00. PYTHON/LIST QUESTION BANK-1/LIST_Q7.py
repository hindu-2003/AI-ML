#Write a Python program to remove duplicates from a list?
nov = int(input("Enter for NUmber of values You wanted for list :"))
if nov<=0:
    print("{} is invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val = input("Enter {} value :".format(i))
        lst.append(val)
    print("Created Your List :{}".format(lst))
    x =(set(lst))
    print("="*50)
print("Removed the Duplicated values from List:{}".format(list(x)))