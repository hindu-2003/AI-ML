#MapFunsEx2.py
oldsal=[100,600,200,300,400,500]
mapobj=map(lambda sal:sal*1.50,oldsal)
print("Type of mapobj=",type(mapobj)) #<class 'map'>
#type cast map object into list object
newsal=list(mapobj)
print("Old Salary List=",oldsal)
print("New Salary List=",newsal)
