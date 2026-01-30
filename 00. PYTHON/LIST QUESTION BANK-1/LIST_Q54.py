#LIST_Q54.py
#Write a Python program to concatenate elements of a list
lst = [val for val in input().split()]
var=""	
for val in lst:
	var =var+ val
clst=[]
clst.append(var)
print(clst)