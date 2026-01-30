#Write a Python program to find the index of an item in a specified list
#LIST_Q22.py
lst = [index for index in input().split()]
print("\t\tindex", "---->", "value")
print("-"*50)
for index,value in enumerate(lst):
    print("\t\t",index,"---->",value)
