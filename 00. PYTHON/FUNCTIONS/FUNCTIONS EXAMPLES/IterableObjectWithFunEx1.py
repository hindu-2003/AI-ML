#IterableObjectWithFunEx1.py
def dispvalues(obj):
    print("type of obj=",type(obj))
    print("Number of values=",len(obj))
    print("-------------------------")
    if(type(obj)==dict):
        for key,val in obj.items():
            print("\t{}-->{}".format(key,val))
    else:
        for val in obj:
            print("\t{}".format(val))
    print("-------------------------")

#Main Program
lst=[10,"Rossum",34.56,2+3j,True]
dispvalues(lst) # function call taking list object
tpl=(100,"Travis",34,56,56,"Python")
dispvalues(tpl) # function call taking tuple object
st={10,20,30,40,50,60,70,80}
dispvalues(st) # function call taking set object
dispvalues(())  # function call taking empty tuple object
dispvalues([])# function call taking empty list object
dispvalues({})# function call taking empty dict object
dispvalues(set())# function call taking empty set object
print("--------------------------------------------")
d={10:"Python",20:"Java",30:"Django",40:"HTML"}
dispvalues(d)