#Write a Python program to get the frequency of the elements in a list.
#LIST_30.py
print("Enter The Numerical Values for create a list:")
lst = [int(val) for val in input().split()]
freq = []
for i in lst:
    x = ((i,i+1))
    freq.append(x)
print(freq)