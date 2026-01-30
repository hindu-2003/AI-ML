#JsonFileToDictObj1.py
import json
with open ("D:\\My\\PYTHON\\LEARN-PYTHON\\JSON\\ST.json","r")as fp:
	d=json.load(fp)
	for k,v in d.items():
		print("{}----{}".format(k,v))

