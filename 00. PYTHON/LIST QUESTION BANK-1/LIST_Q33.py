#Write a Python program to generate all sublists of a list
#LIST_Q33.py
print("Enter The Numerical Values for create a list:")
lst = [(val) for val in input().split()]
lst1 = []
for x in lst:
    lst1.append(x)
    lst1.append(lst)
print("Sub List of lst= ",lst1)