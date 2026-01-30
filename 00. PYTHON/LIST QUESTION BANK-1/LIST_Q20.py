#LIST_Q20.py
#Write a Python program access the index of a list

my_list =[index for index in input().split()]
for index in range(len(my_list)):
    print("Element at index {} is {}".format(index,my_list[index]))
