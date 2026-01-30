#ValueTypeFunEx.py
def decidetype(value):
    if(type(value)==int):
        print("{} is int type value".format(value))
    elif (type(value) == float):
        print("{} is float type value".format(value))
    elif (type(value) == bool):
        print("{} is bool type value".format(value))
    elif (type(value) == complex):
        print("{} is complex type value".format(value))
    elif (type(value) == str):
        print("{} is str type value".format(value))
    elif (type(value) == bytes):
        print("{} is bytes type value".format(value))
    elif (type(value) == bytearray):
        print("{} is bytearray type value".format(value))
    elif (type(value) == range):
        print("{} is range type value".format(value))
    elif (type(value) == list):
        print("{} is list type value".format(value))
    elif (type(value) == tuple):
        print("{} is tuple type value".format(value))
    elif (type(value) == set):
        print("{} is set type value".format(value))
    elif (type(value) == frozenset):
        print("{} is frozenset type value".format(value))
    elif (type(value) == dict):
        print("{} is dict type value".format(value))
    elif type(value) not in [int,float,bool,complex,str,bytes,bytearray,range,list,set,frozenset,dict,tuple]:
           print("{} is None type value".format(value))


#Main Program
decidetype(10)
decidetype(10.2)
decidetype(2+3j)
decidetype(True)
decidetype("PYTHON")
decidetype(bytes([10,20,30,40]))
decidetype(bytearray([10,20,30,40]))
decidetype(range(10,20,2))
decidetype([10,20,30])
decidetype(("Python","Java"))
decidetype({10,20,30})
decidetype(frozenset({10,20}))
decidetype({10:1.2,20:2.3})
decidetype(None)
print("---------------------------------")



