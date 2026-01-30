#LIST_Q19.py
# Write a Python program to get the difference between the two lists
lst1=set([val for val in input().split()])
lst2=set([val for val in input().split()])
lv=(lst1-(lst2))
print(list(lv))
