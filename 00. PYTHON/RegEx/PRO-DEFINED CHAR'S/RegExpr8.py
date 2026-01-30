#Program for Searching for all except Upper Case Alphabets
#RegExpr8.py
import re
print("="*50)
matdet=re.finditer("[^A-Z]","abKp5Dw&8cLq@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)