#Program for Converting JSON String Format into Dict Object
#JsonStrFormatToDictFormat.py
import json
print("-----------------------------------------------------------")
jsonfmt1='{"ENO":"100","NAME":"Rossum","Sal":"5.6"}'  # valid JSON Str Format
print("JSON Data=",jsonfmt1)
print("Type of jsonfmt1=",type(jsonfmt1)) # Type of jsonfmt1= <class 'str'>
#jsonfmt2="{'ENO':'100','NAME':'Rossum','Sal':'5.6'}"----Invalid JSON Str Format--don't use
#Convert json str format into dict object--use loads() of json module
print("-----------------------------------------------------------")
print("Dict Data Converted from JSON Str Format")
print("-----------------------------------------------------------")
d1=json.loads(jsonfmt1)
for fn,fv in d1.items():
		print("{}--->{}".format(fn,fv))
print("-----------------------------------------------------------")
