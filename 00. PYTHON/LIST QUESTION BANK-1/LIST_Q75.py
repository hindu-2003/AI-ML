# LIST_Q75.py
# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 
#	Original list: [1, 1, 2, 3, 4, 4.3, 5, 1]
#	List reflecting the run-length encoding from the said list:
#	[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
#	Original String:
#	automatically
#	List reflecting the run-length encoding from the said string:
#	[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

# demonstrate 1st problem
def word_count(list):

	res = []
	count = 1
	cs = list[0]
	for i in list[1:]:
		if i == cs:
			count = count+1
		else:
			res.append([count,cs])
			cs = i
			count = 1
	res.append([count,cs])
	return res
org_list =  [1, 1, 2, 3, 4, 4.3, 5, 1]
org_str = "automatically"
#main program
print("="*50)
print("List is counted")
print(word_count(org_list))
print("_"*50)
print("word is counted")
print(word_count(org_str))
print("="*50)


	