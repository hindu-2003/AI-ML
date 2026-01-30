# LIST_Q64.py
# 64. Write a Python program to iterate over two lists simultaneously.
# i will use here zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for i1,i2 in zip(list1,list2):
    print("item in list1: {}, item in list2: {}".format(i1,i2))


