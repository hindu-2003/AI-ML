#Write a Python program to find the second smallest number in a list
#LIST_Q27.py
print("Enter the numerical values for list with spaces:")
lst = set([int(val) for val in input().split()])     # 9 8 7 6 5 4 3 2 1
x = list(lst)
x.sort()
print("-"*50)
print("The second smallest number in givel list:{}".format(x[1]))
