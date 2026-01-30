# Write a Python program to clone or copy a list.
#LIST_Q9.PY
nov= int(input("Enter for number of values You want to List:"))
if nov<=0:
    print("{} is invalid input".format(nov))
else:
    lst = []
    for i in range(1,nov+1):
        val = input("Enter  {} value:".format(i))
        lst.append(val)
    print("Orginal list:{}".format(lst))
print("-"*50)
#CLONE THE LIST
clone_list=lst.copy()
print("Cloned list is {}".format(clone_list))
print("-"*50)

# DEEP COPY LIST
Deep_copy = lst
print("Deep copied list is :-{}".format(Deep_copy))

print("="*50)
