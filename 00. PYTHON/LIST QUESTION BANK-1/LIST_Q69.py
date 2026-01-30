#LIST_Q69.py
#69. Write a Python program to remove duplicates from a list of lists.
	#	Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
	#  New List : [[10, 20], [30, 56, 25], [33], [40]]
given_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
E_output =  [[10, 20], [30, 56, 25], [33], [40]]
given_list.sort()
e_list = []
for i in given_list:
    if i in e_list:
        continue
    e_list.append(i)
print("="*50)
print("Exepected output is :{}".format(E_output))
print("   Program output is :{}".format(e_list))
print("="*50)
print("\t EXECUTION COMPLETED")
print("*"*50)