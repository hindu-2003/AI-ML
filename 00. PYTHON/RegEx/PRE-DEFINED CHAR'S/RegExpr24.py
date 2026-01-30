#Program Searching exatcly for zero K or one K or More K's
#RegExpr24.py
import re
matdet=re.finditer("K*","KVKKVKKKVKV")
print("="*50)
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)