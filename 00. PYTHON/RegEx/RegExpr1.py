#RegExpr1.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="Python"
lst=re.findall(sp,gd)
print(lst,type(lst)) # ['Python', 'Python'] <class 'list'>

