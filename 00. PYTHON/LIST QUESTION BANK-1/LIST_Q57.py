#LIST_Q57.py
#57. Write a Python program to check if all items of a given list of strings is equal to a given string.
Gstr = input("Enter a String :")
print("="*50)
print(Gstr)
print("="*50)
lst = Gstr.split()
print(lst)
print("="*50)
for val in lst:
	if Gstr == val:
		print("All items in the list are equal to the given string.")
	else:
		print(" Not all items in the list are equal to the given string.")
print("="*50)