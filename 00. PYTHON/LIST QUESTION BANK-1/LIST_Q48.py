#LIST_Q48.py
# Write a Python program to print a nested lists (each list on a new line) using the print() function.
print("Enter the values with spaces for list with Enter Button and for stop press @ :")
n_list=[]
while("Mahesh"):
    lst1=[val for val in input().split()]
    n_list.append(lst1)
    if lst1 == ["@"]:
        break
n_list.pop()
#print(n_list[:-1])
#print(n_list)
for list in n_list:
    print(list)