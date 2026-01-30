#LIST_Q58.py
#Write a Python program to replace the last element in a list with another list.
	#Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
	#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
print("="*50)
Sample_data = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
print(Sample_data)
print("="*50)
Expected_Output= [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(Expected_Output)
print("="*50)
val = []
for i in Sample_data:
    val.extend(i)
Expected = []
for value in val:
    if value ==10:
        continue
    Expected.append(value)
print(Expected,"\n OUTPUT GOTTEN SUCCESSFULLY")





