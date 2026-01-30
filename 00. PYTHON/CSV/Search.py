#Search.py
import csv
with open('mahi.csv',"r")as fp:
	csvr=csv.reader(fp)
	hname = next(csvr)
	print("-"*50)
	for name in hname:
		print(name,end="\t")
	print()
	print("-"*50)
	for record in csvr:
			for val in record:
				print(val,end="\t")
			print()
		print("-"*50)
	idno=input("Enter Ur Id Number:")
	fp.seek(0)
	res = False
	csvr = csv.reader(fp)
	res = False
	for id in csvr:
		if id:
			if (idno==id[1]):
				res = True
				break
