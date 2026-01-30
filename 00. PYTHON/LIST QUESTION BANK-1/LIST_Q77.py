# LIST_Q77.py
# 77. Write a Python program to decode a run-length encoded given list.
#	Original encoded list:
g_lst=	[[2, 1], 2, 3, [2, 4], 5, 1]
#	Decode a run-length encoded said list:
e_lst=[1, 1, 2, 3, 4, 4, 5, 1]

def encode(lst):
	result = []
	for i in lst:
		if type(i)==int:
			result.append(i)
		else:
			for j in i:
				result.append(j)
	return result
print("Encoded list = ",encode(g_lst))