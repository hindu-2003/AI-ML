#Write a Python program to count the number of elements in a list within a specified range.
# LIST_Q31.py
start = input("Enter range starts :")
end = input("Enter range ends :")
print("Enter The Numerical Values for create a list:")
x =[x for x in input().split() if start < x < end]
print(x)

#x =[x for x in input().split() if start < x < end] within a specified range

