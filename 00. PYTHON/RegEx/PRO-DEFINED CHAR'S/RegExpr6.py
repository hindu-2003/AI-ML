#Program for Searching for all  except 'a' or 'b' or 'c' only
#RegExpr6.py
import re
print("="*50)
matdet=re.finditer("[^abc]","abKp5Dw&8cLq@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)