# LIST_Q63.py
#   63. Write a Python program to insert a given string at the beginning of all items in a list.
# 	Sample list : [1,2,3,4], string : emp
# 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
sample_list = [1,2,3,4]
string = "emp"
Excepect = []
for i in sample_list:
    res = (string+str(i))
    Excepect.append(res)
print(Excepect)