# Write a Python function that takes two lists and returns True if they have at least one common member.
#LIST_Q11.py
print("Enter numerical the values for list 1 ")
lst1=set([list for list in input().split()])

print("Enter numerical the values for list 2 ")
lst2=set([list for list in input().split()])
res=lst1&lst2
if res == set():
    print("No one common elements in above sets \n set1={} \n set2={} ".format(lst1,lst2))
    print("It's Returns to {}".format(res in (lst1 and lst2)))
else:
    print("The common elements are entered sets :{} ".format(res))
    print("It's Returns to {}".format(res not in (lst1 and lst2)))