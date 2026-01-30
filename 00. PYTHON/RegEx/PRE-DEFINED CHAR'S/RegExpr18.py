#Program for Searching  all  except space char(s)
#RegExpr18.py
import re
print("="*50)
matdet=re.finditer(r"\S","ab Kp5Dw&8cL q@6PXzU6!amS")
for mat in matdet:
	print("Start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))
print("="*50)
