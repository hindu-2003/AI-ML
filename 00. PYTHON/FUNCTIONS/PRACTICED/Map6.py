print("Enter the words For First List:")
lst1=[val for val in input().split()]
print("Enter the words For Second List:")
lst2=[val for val in input().split()]
#Now I am waiting for Ur Logic
if(len(lst1)>len(lst2)):
	for i in range(len(lst1)-len(lst2)):
		lst2.append("0")
elif(len(lst2)>len(lst1)):
	for i in range(len(lst2)-len(lst1)):
		lst1.append("0")
else:
    "both are equal "

print(lst1)
print(lst2)
#Now List Values becomes equal and add them by using map()
lst3=(map(lambda x,y: x+y , lst1,lst2))
print("-"*60)
print("\tFirst List\tSecond List\tSum List")
print("-"*60)
for no1,no2,no3 in zip(lst1,lst2,lst3):
	print("\t{}\t\t{}\t\t{}".format(no1,no2,no3))
print("-"*60)