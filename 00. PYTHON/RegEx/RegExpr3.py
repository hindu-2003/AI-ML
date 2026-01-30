#RegExpr3.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="an"
x=re.finditer(sp,gd) # here x is an object callable_iterator
for k in x: # here k is match class type
	print("\tStart Index:{}\tEnd Index:{} \t Value:{}".format(k.start(),k.end(),k.group()))
