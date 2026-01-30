#Program for Searching  lower  Case Alphabets
#RegExpr9.py
import re
print("="*50)
matdet=re.finditer("[a-z]","abKp5Dw&8cLq@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)