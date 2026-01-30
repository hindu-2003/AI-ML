#LIST_Q53.py
# Write a Python program to create a list with infinite elements.
lst = []
print("Enter for Infinite list and stop's for press ---@:")
while(1):
	val = input("Enter Value for list:")
	if val == "@":
		break		
	else:
		lst.append(val)
print(lst)