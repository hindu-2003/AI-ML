#Program for Converting Dict Object into JSON String Format 
#DictObjToJsonStrFormatEx.py
print("------------------------------------------------------------------------")
d1={"ENO":100,"NAME":"Rossum",'Sal':3.4,'Dsg':"Author"}
print("Dict Data =",d1)
print("Type of d1=",type(d1))
print("------------------------------------------------------------------------")
#Convert Dict Object Data into JSON Str Format
jsonfmt=str(d1)
print("Json Data =",jsonfmt)
print("------------------------------------------------------------------------")