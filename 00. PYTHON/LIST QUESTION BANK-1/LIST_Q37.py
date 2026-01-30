# Write a Python program to find common items from two lists
# LIST_37.py
print("Enter The Numerical for create a list:")
lst1 = ([int(val) for val in input().split()])
print("Enter The Numerical for create a list:")
lst2 = ([int(val) for val in input().split()])
s = set(lst1)&set(lst2)
lst3 = list(s)
print("_"*50)
print("Given First List:{}".format(lst1))
print("Given Second List:{}".format(lst2))
print("-"*50)
print("In both list common elements are {}".format(lst3))
print("*"*50)