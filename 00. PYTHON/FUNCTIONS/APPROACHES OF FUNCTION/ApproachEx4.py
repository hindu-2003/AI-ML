#Define a function for Adding of Two Numbers
#ApproachEx4.py
#Input : Taken Inside of Function Body
#Process: Done in Function Body
#Output:  Function Call
def sumop():
    # take input
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Process
    c = a + b
    #Give Result back to function call
    return a,b,c # here return stmt is not only returning one value but also returns more than one value

#main program
k,v,r=sumop() #Function call with Multiline assigment
print("Sum({},{})={}".format(k,v,r))
print("---------------OR-----------------------")
res=sumop() # Function call with single Line assignment
#here res is an object of <class,tuple>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
print("------------------OR----------------------")
print("Sum({},{})={}".format(res[-3],res[-2],res[-1]))


