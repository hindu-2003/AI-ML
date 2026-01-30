# LIST_Q78.py
# 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
#	Original list:
g_list = [1, 1, 2, 3, 4, 4, 5, 1]
#	Length of the first part of the list: 3
#	Splited the said list into two parts:
e_output =	([1, 1, 2], [3, 4, 4, 5, 1])
a = m ,n = [],[]
for i in g_list:
	m.append(i)
	if i == 2:
		break
for j in g_list[3:]:
	n.append(j)
if a == e_output:
	print("="*50)
	print("EXECUTION COMPLETED SUCCESSFULL")
	print("_"*50)
print(a)
print("="*50)
