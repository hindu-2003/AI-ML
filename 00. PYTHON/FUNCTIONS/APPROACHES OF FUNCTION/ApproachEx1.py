#Define a function for Adding of Two Numbers
#ApproachEx1.py
#INPUT  : Taken from Function Call
#PROCESS: Done in Function Body
#RESULT : Function Call
def sumop(a,b): # here a.b are called Formal parameter
    c=a+b
    return c # here c is called local variable
#Main Program
print("type of sumop=",type(sumop)) # type of sumop= <class 'function'>
#Get Two values from KBD
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
res=sumop(k,v) # Function call
print("Sum({},{})={}".format(k,v,res))
