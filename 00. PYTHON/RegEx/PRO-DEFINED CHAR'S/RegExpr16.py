#Program for Searching  all special symbols
#RegExpr16.py
import re
print("="*50)
matdet=re.finditer("[^A-Za-z0-9]","abKp5Dw&8cLq@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)
