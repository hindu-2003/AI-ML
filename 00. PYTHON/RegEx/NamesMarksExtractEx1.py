#Program for Extaracting  Names and  Marks from Given Text
#NamesMarksExtractEx1.py
import re
gd="Rossum is got 66 marks , Gosling got 34 marks , Travis  got 68 marks and Kinney  got 88 marks nad Kvr got 11 marks and Riche got 77 marks"
msp=r"\d{2}"
nsp="[A-Z][a-z]+"
nameslist=re.findall(nsp,gd)
markslist=re.findall(msp,gd)
print("="*50)
print("\tNames\tMarks")
print("="*50)
for names,marks in zip(nameslist,markslist):
	print("\t{}\t{}".format(names,marks))
print("="*50)
