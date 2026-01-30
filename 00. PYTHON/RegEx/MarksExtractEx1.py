#Program for Extaracting the Marks from Given Text
#MarksExtractEx1.py
import re
gd="Rossum is got 66 marks , Gosling got 34 marks , Travis  got 68 marks and Kinney  got 88 marks nad Kvr got 11 marks"
sp=r"\d{2}"
markslist=re.findall(sp,gd)
for marks in markslist:
	print("\t{}".format(marks))
