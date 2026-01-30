#Program Searching for occurences of all chars
#RegExpr26.py
import re
matdet=re.finditer(".","KVKKVKKKVKV")
print("="*50)
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)