# Write a Python program to flatten a shallow list.
#LIST_Q23.py
def shallow(lst1,lst2):
    if(",".join(lst1,lst2)):
        print()
lst1=[val for val in input().split()]
lst2=[val for val in input().split()]
lst1.append(lst2)
res = lst1
print(shallow(lst1,lst2))
