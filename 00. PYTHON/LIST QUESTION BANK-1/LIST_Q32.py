# Write a Python program to check whether a list contains a sublist
#LIST_Q32.py
print("Enter the values for 1st List:")
lst1 = [(val) for val in input().split()]
print("Enter the values for 2nd List:")
lst2 = [(val) for val in input().split()]
cp = list(map(lambda x,y:x == y ,lst1,lst2))
if cp == True:
    print("list contains a sublist")
else:
    print("list not contains a sublist")


