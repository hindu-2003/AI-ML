#JsonStrFormatToDictFormat1.py
import json
jsonstr = '{"Eno":10,"Ename":"mahesh","Esal":1000}'
d = json.loads(jsonstr)
print(d)
print(type(d))
