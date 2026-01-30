# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# 	Sample list: [0,1,2,3,4,5]
# 	Expected Output: [1, 0, 3, 2, 5, 4]
# LIST_Q38.py
list= [int(val) for val in input("Enter the value for list:").split()]
print(list)
for i in range(0,len(list),2):
    list[i],list[i+1]=list[i+1],list[i]
print(list)


