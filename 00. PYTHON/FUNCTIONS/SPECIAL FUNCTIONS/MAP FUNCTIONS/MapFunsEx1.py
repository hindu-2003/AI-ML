#MapFunsEx1.py
def hike(sal): # Normal function
    return (sal+sal*(50/100))

#Main Program
oldsal=[100,600,200,300,400,500]
mapobj=map(hike,oldsal)
print("Type of mapobj=",type(mapobj)) #<class 'map'>
#type cast map object into list object
newsal=list(mapobj)
print("Old Salary List=",oldsal)
print("New Salary List=",newsal)
