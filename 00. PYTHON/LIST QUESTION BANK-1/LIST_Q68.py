#LIST_Q68.py
#68. Write a Python program to extend a list without append.      
#	Sample data: [10, 20, 30],[40, 50, 60]
#	Expected output : [40, 50, 60, 10, 20, 30]
s_data =  [10, 20, 30],[40, 50, 60]
e_data =  [40, 50, 60, 10, 20, 30]
print("_"*50)
print("\tExpected output : [40, 50, 60, 10, 20, 30]")
e = []
for i in s_data[::-1]:
	e.extend(i)
print("*"*50)
print("\t Program output :",e)
print("_"*50)
if e == e_data:
	print("\tEXECUTION COMPLETED")
print("*"*50)


