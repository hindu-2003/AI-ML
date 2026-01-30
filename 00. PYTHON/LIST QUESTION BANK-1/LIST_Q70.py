#LIST_Q70.py
#70. Write a Python program to find the items starts with specific character from a given list. 
#	Expected Output:
#		Original list:
#		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#     Items start with a from the said list:
#  	['abcd', 'abc', 'acjd']
#		Items start with d from the said list:
#		['dagfa']
#		Items start with w from the said list:
#		[]
given_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
sa = []
sd = []
sw = []
for i in given_list:
	if i.startswith("a"):
		sa.append(i)
	if i.startswith("d"):
		sd.append(i)
	if i.startswith("w"):
		sw.append(i)

print("="*50)
print("Items start with a from the said list:{}".format(sa))
print("Items start with d from the said list:{}".format(sd))
print("Items start with w from the said list:{}".format(sw))
print("="*50)
