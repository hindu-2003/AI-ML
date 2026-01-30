# Write a Python program to get unique values from a list
# LIST_Q29.py
def unique_values(x):
    return list(set(x))
print("Enter The Numericals for create a list:")
lst = [int(val) for val in input().split()]
unique = unique_values(lst)
print("_"*50)
print("Given List:{}".format(lst))
print("-"*50)
print("Unique values are:", unique)
print("*"*50)

