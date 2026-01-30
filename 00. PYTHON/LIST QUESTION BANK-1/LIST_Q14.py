# Write a Python program to print the numbers of a specified list after removing even numbers from it.
lst=[val for val in input().split() if int(val)%2==1]
print("Removed the even numbers above list:{}".format(lst))
print("----------------OR------------------")
nov = int(input("Number of values U want in list :"))
if nov<=0:
    print("{} is invalid input".format(nov))
else:
    list=[]
    even=[]
    with_out_even=[]
    for x in range(1,nov+1):
        odd=input("Enter {} the value:".format(x))
        list.append(odd)
        if int(odd)%2==0:
            even.append(odd)
        else:
            with_out_even.append(odd)
print("-"*50)
print("Given list:{}".format(list))
print()
print("Removed the even numbers the above list :{}".format(with_out_even))
print("*"*50)
