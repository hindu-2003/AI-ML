#Write a Python program to select the odd items of a list
#LIST_Q46.py

print("_"*50)
print("Enter the Numerical values for list with space :")
s = [int(val) for val in input().split() if int(val)%2!=0]
print("_"*50)
print("Odd numbers are Given List")
print(s)
print("="*50)



