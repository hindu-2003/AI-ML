#Program for Reading JSON File Data into Dict Object
#JsonFileToDictObj.py
import json
try:
	with open("c:\\stud.json","r") as fp:
			d=json.load(fp)
			for k,v in d.items():
				print("{}--->{}".format(k,v))
except FileNotFoundError:
	print("JSON File Does not Exist")