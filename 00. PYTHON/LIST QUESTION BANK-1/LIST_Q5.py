# #5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2
#LIST_Q5.py
nov = int(input("Enter how many values u are u want:"))
if nov<=0:
    print("PLease enter least one value for list creation")
else:
    slst = []
    lst = []
for i in range(1,nov+1):
    val = (input("enter {} the values:".format(i)))
    lst.append(val)
print("-"*50)
print("\tList is created {}".format(lst))
print("*"*50)
for j in lst:
    if j == j[::-1]:
        slst.append(j)
print("first and last character are same from a given list of strings: {}".format(len(slst)))
print("*"*50)
