#RegExpr4.py
import re
gd="abKp5Dw&8cLq@6PXzU6!amS"
sp=re.compile("[abc]")
print("="*50)
matdet=re.finditer(sp,gd)
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)