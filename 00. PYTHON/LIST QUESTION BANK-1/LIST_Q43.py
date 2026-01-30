#LIST_Q43.py
# Write a Python program to split a list into different variables
print("Enter Values for list with spaces:")
lst = [val for val in input().split()]
var=[]
for i in range(0,len(lst)):
    v = input("Enter {} value for variable:".format(lst[i]))
    var.append(v)
print(var)
print("split a list into different variables")
print("Created by Dynamic list:",(lst))
m = ""
l = []
for i in var:
    m = m+ i
for j in lst:
    l.append(j)
m = l
print("="*50)
for h in range(len(m)):
    print("\t\t\t{} = {}".format(var[h],l[h]))
print("=" * 50)