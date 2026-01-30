#Program for Saving Dict Data into the JSON File
#DictObjToJsonFile.py
import json
#take dict object Data
d1={"SNO":100,"NAME":"TRavis","Marks":8.5,"ColName":"OUCET"}
#Save the Dict Data into JSON File
with open("c:\\stud.json","a") as fp:
	json.dump(d1,fp)
	print("Dict Data written to the JSON File")
