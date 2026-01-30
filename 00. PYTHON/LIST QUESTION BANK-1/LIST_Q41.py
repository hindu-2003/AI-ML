# LIST_Q41.py
# # Write a Python program to create multiple lists
num_lists = int(input("Enter the how many items in list You want :"))
if num_lists <= 0:
    print("{} it is invalid input ---Try again")
else:
    nl = []
    for i in range(1,num_lists+1):
        val=input("Enter the {} value:".format(i))
        nl.append(val)
lists = list(nl)
for i, value in enumerate(nl):
    lists[i] = (nl)
print(lists)
