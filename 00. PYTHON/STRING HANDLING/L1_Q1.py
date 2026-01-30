#Write a Python program to sum all the items in a list.
n = int(input("Enter The numbers for sum all the items in a list:"))
lst = []
if n.isdigit():
	lst = lst+n
	print(lst)