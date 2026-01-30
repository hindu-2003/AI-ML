# Define a Function for calculating Sum of Two Numbers
#AnonymousFunEx1.py
def sumop(a,b): # Normal Function
    return (a+b)

addop = lambda k,v : k+v # Anonymous Function

#Main Program
print("type of sumop=",type(sumop)) # <class,'function'>
res1=sumop(100,200) # Normal Function Call
print("sum by using Normal Fun=",res1)
print("----------------------------------")
print("type of addop=",type(addop)) # <class,'function'>
res2=addop(1000,2000) # Anonymous Function Call
print("sum by using Anonymous Function=",res2)
print("-----------------------------------------")
print("Enter Two Values")
a,b=float(input()),float(input())
r=addop(a,b) # Anonymous Function Call
print("sum({},{})={}".format(a,b,r))