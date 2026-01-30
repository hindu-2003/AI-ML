#Program for Extaracting the Names from Given Text
#NamesExtractEx1.py
import re
gd="Rossum is dev of python , Gosling the dev of java , Travis is the dev of numpy and Kinney is the dev of pandas and Kvr is trainer of python"
sp="[A-Z][a-z]+"
names=re.findall(sp,gd)
print("List of Names:")
for name in names:
	print("\t{}".format(name))
