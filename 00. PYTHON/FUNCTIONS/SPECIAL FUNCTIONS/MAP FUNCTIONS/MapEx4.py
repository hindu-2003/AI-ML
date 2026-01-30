#Program for Finding Sum of Two List Objects
#MapEx4.py
print("Enter the Numerical For First List:")
lst1=[float(val) for val in input().split()]
print("Enter the Numerical For Second List:")
lst2=[float(val) for val in input().split()]
lst3=list(map(lambda x,y: x+y, lst1,lst2))
print("-"*60)
print("\tFirst List\tSecond List\tSum List")
print("-"*60)
for no1,no2,no3 in zip(lst1,lst2,lst3):
	print("\t{}\t\t{}\t\t{}".format(no1,no2,no3))
print("-"*60)