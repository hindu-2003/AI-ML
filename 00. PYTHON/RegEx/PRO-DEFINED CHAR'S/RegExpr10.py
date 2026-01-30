#Program for Searching  all except lower  Case Alphabets
#RegExpr10.py
import re
print("="*50)
matdet=re.finditer("[^a-z]","abKp5Dw&8cLq@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)