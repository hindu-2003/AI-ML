#Program Searching exatcly for one K at a time
#RegExpr22.py
import re
matdet=re.finditer("K","KVKKVKKKVKV")
print("="*50)
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)