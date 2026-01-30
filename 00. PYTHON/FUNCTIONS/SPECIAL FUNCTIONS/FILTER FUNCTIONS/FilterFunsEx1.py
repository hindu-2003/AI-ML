#Program for Obtaining +ve Elements from list of values
#FilterFunsEx1.py
def positive(val): # Normal Function
    if(val>0):
        return True
    else:
        return False
def negative(val): # Normal Function
    return True if val<0 else False

#Main Program
lst=[10,20,-30,40,-67,23,-7,0,12]
filterobj1=filter(positive,lst) # here kvr is an object of <class 'filter'>
filterobj2=filter(negative,lst)
print("type of filterobj1=",type(filterobj1))
#When we display an object of filter, we are getting Its memory address.
#So get the content of Filter Object, we must type cast to any Iterable object
pslist=list(filterobj1)
nglist=tuple(filterobj2)
print("Given Values=",lst)
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)