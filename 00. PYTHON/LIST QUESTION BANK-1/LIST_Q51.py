#LIST_Q51.py
# Write a Python program to split a list every Nth element. 
	#Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
	#Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

Given_List =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected_Output = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
Expected = []
l1 = Given_List[::3]
l2 = Given_List[1::3]
l3 = Given_List[2::3]
Expected.append(l1)
Expected.append(l2)
Expected.append(l3)
print(Expected)
if Expected==Expected_Output:
	print('Program Execution is completed successful')
	print('\t\t THANK YOU')
else:
	print("Your output Doesn't match --try again")


