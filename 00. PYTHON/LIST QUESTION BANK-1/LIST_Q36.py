#Write a Python program to get variable unique identification numbeor string
#LIST_Q36.py
print("Enter The Numericals for create a list:")
lst1 = set([int(val) for val in input().split()])
print("Enter The Numericals for create a list:")
lst2 = set([int(val) for val in input().split()])
lst1^lst2
print(lst1)