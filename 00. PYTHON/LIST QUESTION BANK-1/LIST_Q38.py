# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# 	Sample list: [0,1,2,3,4,5]
# 	Expected Output: [1, 0, 3, 2, 5, 4]
# LIST_Q38.py
def swap(lst):
    for i in range(0,len(lst)-1,2):
        lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
# Sample usage:
list = [0, 1, 2, 3, 4]
expected_output = swap(list)
print(expected_output)  # [1, 0, 3, 2, 5, 4]
