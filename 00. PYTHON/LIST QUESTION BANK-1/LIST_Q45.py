#  Write a Python program to convert a pair of values into a sorted unique array
# LIST_Q45.py
print("Enter the numerical values for list : ")
lst = [int(val) for val in input().split()]
st = set(lst)
k = list(st)
k.sort()
print(k)