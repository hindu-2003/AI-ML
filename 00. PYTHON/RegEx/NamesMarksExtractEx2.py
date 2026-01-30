#Program for Extaracting  Names and  Marks from Given File (Student.data)
#NamesMarksExtractEx2.py
import re
try:
	with open("E:\\KVR-PYTHON-6PM\\REG EXPR\\NOTES\\student.data","r") as fp:
		filedata=fp.read()
		nameslist=re.findall(r"[A-Z][a-z]+",filedata)
		markslist=re.findall(r"\d{2}",filedata)
		print("="*50)
		print("\tNames\tMarks")
		print("="*50)
		for names,marks in zip(nameslist,markslist):
			print("\t{}\t{}".format(names,marks))
		print("="*50)
except FileNotFoundError:
	print("File does not Exist")

