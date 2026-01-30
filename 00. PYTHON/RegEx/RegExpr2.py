#RegExpr2.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="Python"
mat=re.search(sp,gd)
if(mat!=None):
	print("Search is sucessful") # here mat is an object of class <re.match >
	print("Start Value:",mat.start()) # 0
	print("End Value:",mat.end()) # 6
	print("Value=",mat.group()) # python
else:
	print("Search is Un-Sucessful")

